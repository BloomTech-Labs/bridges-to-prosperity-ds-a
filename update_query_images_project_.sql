update public."Bridges"

set bridge_image = public."temp_project_url".bridge_image

from  public."temp_project_url"

where public."Bridges".project_code = public."temp_project_url".project_code
