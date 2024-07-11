FROM odoo:15.0

COPY ./config/odoo.conf /etc/odoo/
COPY ./custom-addons /mnt/extra-addons

# Install custom dependencies if needed
RUN pip install -r /mnt/extra-addons/requirements.txt

# Set permissions
RUN chown -R odoo:odoo /mnt/extra-addons

USER odoo
