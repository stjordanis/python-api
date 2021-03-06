from ravenpackapi import RPApi

api = RPApi()

# get the list of the uploaded files
for f in api.upload.list():
    # here we can access the file - see below for the options
    print(f)

# upload a file to access the analytics
f = api.upload.file("_orig.doc",
                    # properties={"primary_entity": "RavenPack"}
                    )
f.wait_for_completion()

# we can also get it if we know the id
# f = api.upload.get('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

# get back the analytics found in the document
f.save_analytics("_analytics.json")

# the annotated version
f.save_annotated("us30orig.xml")

# or the original
f.save_original("_orig.doc")

# given a file we can set tags
# f.set_metadata(tags=['file tag'])

# ... or delete it
# f.delete()

# we can also work with folders
folder = api.upload.folder_create('documents')
print(folder)
folder.folder_name = "papers"
folder.save()

# upload a file into a folder:
f = api.upload.file("_orig.doc", folder=folder)
