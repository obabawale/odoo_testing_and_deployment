FROM odoo:15.0

COPY ./config/odoo.conf /etc/odoo/

USER root 

COPY ./custom-addons /mnt/extra-addons

# Install custom dependencies if needed
RUN pip install -r /mnt/extra-addons/requirements.txt

# Set permissions
RUN chown -R odoo:odoo /mnt/extra-addons

USER odoo

# FROM odoo:15.0

# USER root

# COPY ./altrad-erp-project/requirements.txt .

# RUN apt -y update && pip install -r requirements.txt --no-cache-dir

# USER odoo
