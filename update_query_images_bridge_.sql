update public."Bridges"

set bridge_image = public."temp_bridge_url".bridge_image

from  public."temp_bridge_url"

where public."Bridges".name = public."temp_bridge_url".name
