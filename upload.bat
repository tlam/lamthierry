set PYTHONPATH=C:\django_proj\lamthierry
appcfg.py upload_data --config_file=lamthierry/skill_loader.py --filename=skill_data.csv --kind=Skill --email=lamthierry@gmail.com --url=http://localhost:8080/load lamthierry
rem appcfg.py upload_data --config_file=lamthierry/skill_loader.py --filename=skill_data.csv --kind=Skill lamthierry
rem appcfg.py upload_data --config_file=lamthierry/myprofile/skill_loader.py --filename=lamthierry/data/skill_data.csv --kind=Skill lamthierry
rem bulkload_client.py --filename=skill_data.csv --kind=Skill --url=http://localhost:8080/load
