

let admin_users_exists = db.getCollectionNames().includes('admin_users');
if(!admin_users_exists) {
    db.createCollection("admin_users", {
        validator : {
            $jsonSchema : {
                bsonType : "object", 
                required : ["email", "username"],
                properties : {
                    email : {
                        bsonType : "string",
                        description : "must be a string and is required"
                    },
                    username : {
                        bsonType : "string",
                        description : "must be an integer, value should be less than 18 and required"
                    }
                }
            }
        },
        validationLevel : "strict",
        validationAction : "error"     
     });
 
    db.getCollection('admin_users').createIndex({"email" : 1}, {unique: true});
}

let acl_role_exists = db.getCollectionNames().includes('acl_roles');

if(!acl_role_exists) {
    db.createCollection("acl_roles", {
        validator : {
            $jsonSchema : {
                bsonType : "object", 
                required : ["role_name"],
                properties : {
                    role_name : {
                        bsonType : "string",
                        description : "must be a string and is required"
                    }
                }
            }
        },
        validationLevel : "strict",
        validationAction : "error"     
    });
     
     
    db.getCollection('acl_roles').createIndex({"role_name" : 1}, {unique: true});
}
