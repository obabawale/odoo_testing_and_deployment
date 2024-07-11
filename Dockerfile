FROM odoo:15.0

COPY config/odoo.conf /etc/odoo/

USER root 

COPY custom-addons /mnt/extra-addons

COPY odoo_pg_pass .

# Install custom dependencies if needed
# RUN pip install -r /mnt/extra-addons/requirements.txt

# Set permissions
RUN chown -R odoo:odoo /mnt/extra-addons

USER odoo

