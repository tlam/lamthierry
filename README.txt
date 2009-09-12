# Uploading data to dev datastore
C:\web_dev>appcfg.py upload_data --config_file=lamthierry\myprofile\skill_loader.py --email=lamthierry@gmail.com --filename=lamthierry\data\skill_data.csv --kind=Skill --url=http://localhost:8080/load lamthierry
C:\web_dev>appcfg.py upload_data --config_file=lamthierry\portfolios\portfolio_loader.py --email=lamthierry@gmail.com --filename=lamthierry\data\portfolio_data.csv --kind=Portfolio --url=http://localhost:8080/load lamthierry

# Uploading data to live datastore
appcfg.py upload_data --config_file=lamthierry\myprofile\skill_loader.py --filename=lamthierry\data\skill_data.csv --kind=Skill lamthierry
appcfg.py upload_data --config_file=lamthierry\portfolios\portfolio_loader.py --filename=lamthierry\data\portfolio_data.csv --kind=Portfolio lamthierry
