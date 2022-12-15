
###
# Main application interface
###
from flask import Flask, jsonify, request
from flaskext.mysql import MySQL

# import the create app function 
# that lives in src/__init__.py
from src import create_app
from src import db

# profile being displayed to user
currentProfileNum = 1
totalUserCount = 0
# current main user interacting with site
currentUsername = ""


# create the app object
app = create_app()

@app.route('/db_test', methods = ['GET'])
def db_test():
   cur = db.get_db().cursor()
   cur.execute('select * from main_user')
   row_headers = [x[0] for x in cur.description]
   json_data = []
   theData = cur.fetchall()
   for row in theData:
       json_data.append(dict(zip(row_headers, row)))
   return jsonify(json_data)

@app.route('/get_matches', methods = ['GET'])
def get_matches():
   cur = db.get_db().cursor()
   cur.execute('select * from matched_profiles')
   row_headers = [x[0] for x in cur.description]
   json_data = []
   theData = cur.fetchall()
   for row in theData:
       json_data.append(dict(zip(row_headers, row)))
   return jsonify(json_data)

@app.route('/get_matchData_main_user', methods = ['GET'])
def matchData_user():
    cur = db.get_db().cursor()
    app.logger.info(request.form)
    username = request.form['username']
    json_data = []

    query = f'SELECT userID from main_user where username = \'{username}\''
    cur.execute(query)
    currentMainUserID = 0
    theData = cur.fetchall()
    if len(theData) != 0:
        currentMainUserID = theData[0][0]
    
    if currentMainUserID == 0:
        return jsonify(json_data.append(dict(name = "Error")))
    
    query = f'SELECT matchedProfileID from matched_profiles where main_userID = {currentMainUserID}'
    cur.execute(query)
    theData = cur.fetchall()
    c = 0
    if len(theData) == 0:
        text = "Nobody, keep trying"
        json_data.append(dict(name = text))
        return jsonify(json_data)

    for row in theData:
        id = theData[c][0]
        c += 1
        query = f'SELECT * from main_user where userID = {id}'
        cur.execute(query)
        matchData = cur.fetchall()
        row_headers = [x[0] for x in cur.description]
        for row in matchData:
            json_data.append(dict(zip(row_headers, row)))
    
    return jsonify(json_data)

@app.route('/get_liked_profiles', methods = ['GET'])
def liked_profiles():
   cur = db.get_db().cursor()
   cur.execute('select * from liked_profiles')
   row_headers = [x[0] for x in cur.description]
   json_data = []
   theData = cur.fetchall()
   for row in theData:
       json_data.append(dict(zip(row_headers, row)))
   return jsonify(json_data)

@app.route('/get_disliked_profiles', methods = ['GET'])
def disiked_profiles():
   cur = db.get_db().cursor()
   cur.execute('select * from disliked_profiles')
   row_headers = [x[0] for x in cur.description]
   json_data = []
   theData = cur.fetchall()
   for row in theData:
       json_data.append(dict(zip(row_headers, row)))
   return jsonify(json_data)

@app.route('/get_usernames', methods = ['GET'])
def get_usernames():
   cur = db.get_db().cursor()
   cur.execute('select username as label, username as value from main_user')
   row_headers = [x[0] for x in cur.description]
   json_data = []
   theData = cur.fetchall()
   for row in theData:
       json_data.append(dict(zip(row_headers, row)))     
   return jsonify(json_data)


@app.route('/create_profile', methods = ['POST']) 
def create_profile():
    app.logger.info(request.form)
    cur = db.get_db().cursor()
    user = request.form['username']
    password = request.form['password']
    name = request.form['name']
    city = request.form['city']
    state = request.form['state']
    age = request.form['age']
    gender = request.form['gender']
    datingPref = request.form['datingPref']
    phoneNumber = request.form['phoneNumber']
    description = request.form['description']
    global currentUsername
    currentUsername = user
    query = f'''INSERT INTO main_user (username, password, name, city, state, age, gender, phoneNumber, description, datingPref)
        VALUES (\"{user}\", \"{password}\", \"{name}\", \"{city}\", \"{state}\", \"{age}\", \"{gender}\", \"{phoneNumber}\", \"{description}\", \"{datingPref}\")'''
    
    
    cur.execute(query)

    return "success!"

@app.route('/delete_user', methods = ['DELETE'])       
def deleteUser():
    args = request.args
    username = args.get('username')
    cur = db.get_db().cursor()
    query = f'DELETE FROM main_user WHERE main_user.username = \"{username}\"'
    cur.execute(query)

    return "success!"

@app.route('/del_liked_pair', methods = ['DELETE'])       
def deleteLikedPair():
    app.logger.info(request.form)
    cur = db.get_db().cursor()
    mainProfID = request.form['main_userID']
    likedProfID = request.form['liked_profileID']
    query = f'DELETE FROM liked_profiles where main_userID = {mainProfID} and likedProfileID = {likedProfID}'
    
    cur.execute(query)

    return "success!"

@app.route('/del_disliked_pair', methods = ['DELETE'])       
def deleteDisLikedPair():
    app.logger.info(request.form)
    cur = db.get_db().cursor()
    mainProfID = request.form['main_userID']
    dislikedProfID = request.form['disliked_profileID']
    query = f'DELETE FROM disliked_profiles where main_userID = {mainProfID} and dislikedProfileID = {dislikedProfID}'
    
    cur.execute(query)
    return "success!"

@app.route('/delete_match', methods = ['DELETE'])       
def deleteMatch():
    app.logger.info(request.form)
    cur = db.get_db().cursor()
    mainProfID = request.form['main_userID']
    matchedProfID = request.form['matchedProfileID']
    query = f'DELETE FROM matched_profiles where main_userID = {mainProfID} and matchedProfileID = {matchedProfID}'
    
    cur.execute(query)

    return "success!"

@app.route('/store_currentUser', methods = ['PUT'])
def storeUser():
    args = request.args
    username = args.get('username')
    global currentUsername
    global currentProfileNum
    currentUsername = username
    currentProfileNum = 1
    return "Success!"

@app.route('/getActionProfileData', methods = ['GET'])
def getActionProfileData():
    cur = db.get_db().cursor()
    cur.execute('select COUNT(*) from main_user')
    json_data = []
    theData = cur.fetchall()
    totalUsers = theData[0][0]
    global totalUserCount
    global currentProfileNum
    totalUserCount = totalUsers
    json_data.append(dict(id = currentProfileNum))
    json_data.append(dict(userCount = totalUsers))

    offset = currentProfileNum - 1
    query = f'SELECT userID FROM main_user LIMIT 1 OFFSET {offset}'
    cur.execute(query)
    theData = cur.fetchall()
    currentProfileId = theData[0][0]

    query = f'select * from main_user where userID = {currentProfileId}'
    cur.execute(query)
    row_headers = [x[0] for x in cur.description]
    theData = cur.fetchall()
    for row in theData:
       json_data.append(dict(zip(row_headers, row)))
    
    return jsonify(json_data)

@app.route('/like_profile', methods = ['POST', 'GET']) 
def like_profile():
    global currentProfileNum
    app.logger.info(request.form)
    cur = db.get_db().cursor()
    json_data = []

    username = request.form['username']
    query = f'SELECT userID from main_user where username = \'{username}\''
    cur.execute(query)
    currentMainUserID = 0
    theData = cur.fetchall()
    if len(theData) != 0:
        currentMainUserID = theData[0][0]

    offset = currentProfileNum - 1
    query = f'SELECT userID FROM main_user LIMIT 1 OFFSET {offset}'
    cur.execute(query)
    theData = cur.fetchall()
    currentProfileId = theData[0][0]
    
    alrExists = 0 # 0 means false
    queryExists = f'SELECT EXISTS (SELECT * from liked_profiles where main_userID = {currentMainUserID} and likedProfileID = {currentProfileId})'
    if currentMainUserID != 0:
        cur.execute(queryExists)
        theData = cur.fetchall()
        alrExists = theData[0][0]
    
    query = f'insert into liked_profiles (main_userID, likedProfileID) VALUES ({currentMainUserID}, {currentProfileId})'
    if currentMainUserID != currentProfileId and alrExists == 0:
        cur.execute(query)
        json_data.append(dict(addedToTable = currentProfileId))
        updateMatches(currentMainUserID, currentProfileId)
    currentProfileNum = currentProfileNum + 1
    if totalUserCount < currentProfileNum:
        currentProfileNum = 1
    
    json_data.append(dict(currMainId = currentMainUserID))
    json_data.append(dict(currProfId = currentProfileId))
    json_data.append(dict(currProfNumber = currentProfileNum))

    return jsonify(json_data)

@app.route('/dislike_profile', methods = ['POST', 'GET']) 
def dislike_profile():
    global currentProfileNum
    app.logger.info(request.form)
    cur = db.get_db().cursor()
    json_data = []

    username = request.form['username']
    query = f'SELECT userID from main_user where username = \'{username}\''
    cur.execute(query)
    currentMainUserID = 0
    theData = cur.fetchall()
    if len(theData) != 0:
        currentMainUserID = theData[0][0]

    offset = currentProfileNum - 1
    query = f'SELECT userID FROM main_user LIMIT 1 OFFSET {offset}'
    cur.execute(query)
    theData = cur.fetchall()
    currentProfileId = theData[0][0]
    
    alrExists = 0 # 0 means false
    queryExists = f'SELECT EXISTS (SELECT * from disliked_profiles where main_userID = {currentMainUserID} and dislikedProfileID = {currentProfileId})'
    if currentMainUserID != 0:
        cur.execute(queryExists)
        theData = cur.fetchall()
        alrExists = theData[0][0]
    
    query = f'insert into disliked_profiles (main_userID, dislikedProfileID) VALUES ({currentMainUserID}, {currentProfileId})'
    if currentMainUserID != currentProfileId and alrExists == 0:
        cur.execute(query)
        json_data.append(dict(addedToTable = currentProfileId))
    
    currentProfileNum = currentProfileNum + 1
    if totalUserCount < currentProfileNum:
        currentProfileNum = 1
    
    json_data.append(dict(currMainId = currentMainUserID))
    json_data.append(dict(currProfId = currentProfileId))
    json_data.append(dict(currProfNumber = currentProfileNum))

    return jsonify(json_data)

def updateMatches(mainUserID, profileID):
    # check if opposite exists in likedProfles
    # if it does create match for both profiles in matches table
    cur = db.get_db().cursor()
    alrExists = 0 # 0 means false
    queryExists = f'SELECT EXISTS (SELECT * from liked_profiles where main_userID = {profileID} and likedProfileID = {mainUserID})'
    cur.execute(queryExists)
    theData = cur.fetchall()
    if len(theData) != 0:
        alrExists = theData[0][0]
    if alrExists == 1:
        query = f'insert into matched_profiles (main_userID, matchedProfileID) values ({profileID}, {mainUserID})'
        cur.execute(query)
        query = f'insert into matched_profiles (main_userID, matchedProfileID) values ({mainUserID}, {profileID})'
        cur.execute(query)

    return "Success!"

@app.route('/flag_description', methods = ['POST']) 
def flag_desc():
    app.logger.info(request.form)
    cur = db.get_db().cursor()
    username = request.form['username']
    query =f'UPDATE main_user set isFlagged = {1} where username = \'{username}\''
    cur.execute(query)

    return "success!"

@app.route('/unflag_description', methods = ['POST']) 
def unflag_desc():
    app.logger.info(request.form)
    cur = db.get_db().cursor()
    username = request.form['username']
    query =f'UPDATE main_user set isFlagged = {0} where username = \'{username}\''
    cur.execute(query)

    return "success!"

if __name__ == '__main__':
    # we want to run in debug mode (for hot reloading) 
    # this app will be bound to port 4000. 
    # Take a look at the docker-compose.yml to see 
    # what port this might be mapped to... 
    app.run(debug = True, host = '0.0.0.0', port = 4000)