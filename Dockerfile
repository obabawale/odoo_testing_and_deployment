FROM odoo:15.0

COPY ./config/odoo.conf /etc/odoo/

RUN more /etc/odoo/odoo.conf

USER root 

COPY custom-addons /mnt/extra-addons

# Install custom dependencies if needed
# RUN pip install -r /mnt/extra-addons/requirements.txt

# Set permissions
RUN chown -R odoo:odoo /mnt/extra-addons

# List the contents of /mnt/extra-addons
RUN ls -l /mnt/extra-addons

USER odoo
