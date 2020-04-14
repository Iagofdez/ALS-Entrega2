#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2

class MainHandler(webapp2.RequestHandler):
    def post(self):
        CIFEm = self.request.get("edCIF", "Desconocido")
        DireccionEm = self.request.get("edDireccion", "Desconocido")
        PoblacionEm = self.request.get("edPoblacion", "Desconocido")
        ProvinciaEm = self.request.get("edProvincia", "Desconocido")
        CPEm = self.request.get("edCP", "Desconocido")
        PaisEm = self.request.get("edPais", "Desconocido")
        ContactoEm = self.request.get("edContacto", "Desconocido")
        EmailEm = self.request.get("edEmail", "Desconocido")
        TelefonoEm = self.request.get("edTelefono", "Desconocido")
        CIFCliente = self.request.get("edCIF", "Desconocido")
        DireccionCliente = self.request.get("edDireccion", "Desconocido")
        TelefonoCliente = self.request.get("edTelefono", "Desconocido")
        PoblacionCliente = self.request.get("edPoblacion", "Desconocido")
        ProvinciaCliente = self.request.get("edProvincia", "Desconocido")
        CPCliente = self.request.get("edCP", "Desconocido")
        PaisCliente = self.request.get("edPais", "Desconocido")
        ContactoCliente = self.request.get("edContacto", "Desconocido")
        EmailCliente = self.request.get("edEmail", "Desconocido")
        Concepto = self.request.get("edConcepto", "Desconocido")
        Precio = self.request.get("edPrecio", "Desconocido")
        Unidades = self.request.get("edUnidades", "Desconocido")
        ImporteBruto = str(float(Precio) * float(Unidades))
        IVA = self.request.get("edIVA", "Desconocido")
        ImporteTotal = str(float(ImporteBruto) * (1 + float(IVA)))

        if len(CIFEm.strip()) == 0:
            CIFEm = "Desconocido"
        if len(DireccionEm.strip()) == 0:
            DireccionEm = "Desconocido"
        if len(PoblacionEm.strip()) == 0:
            PoblacionEm = "Desconocido"
        if len(ProvinciaEm.strip()) == 0:
            ProvinciaEm = "Desconocido"
        if len(CPEm.strip()) == 0:
            CPEm = "Desconocido"
        if len(PaisEm.strip()) == 0:
            PaisEm = "Desconocido"
        if len(ContactoEm.strip()) == 0:
            ContactoEm = "Desconocido"
        if len(EmailEm.strip()) == 0:
            EmailEm = "Desconocido"
        if len(TelefonoEm.strip()) == 0:
            TelefonoEm = "Desconocido"
        if len(CIFCliente.strip()) == 0:
            CIFCliente = "Desconocido"
        if len(DireccionCliente.strip()) == 0:
            DireccionCliente = "Desconocido"
        if len(PoblacionCliente.strip()) == 0:
            PoblacionCliente = "Desconocido"
        if len(ProvinciaCliente.strip()) == 0:
            ProvinciaCliente = "Desconocido"
        if len(CPCliente.strip()) == 0:
            CPCliente = "Desconocido"
        if len(PaisCliente.strip()) == 0:
            PaisCliente = "Desconocido"
        if len(ContactoCliente.strip()) == 0:
            ContactoCliente = "Desconocido"
        if len(EmailCliente.strip()) == 0:
            EmailCliente = "Desconocido"
        if len(TelefonoCliente.strip()) == 0:
            TelefonoCliente = "Desconocido"
        if len(Concepto.strip()) == 0:
            Concepto = "Desconocido"
        if Precio == 0:
            Precio = "Desconocido"
        if Unidades == 0:
            Unidades = "Desconocido"
        if ImporteBruto == 0:
            ImporteBruto = "Desconocido"
        if IVA == 0:
            IVA = "Desconocido"
        if ImporteTotal == 0:
            ImporteTotal = "Desconocido"

        valores_plantilla = {
            "CIFEm": CIFEm,
            "DireccionEm": DireccionEm,
            "PoblacionEm": PoblacionEm,
            "ProvinciaEm": ProvinciaEm,
            "CPEm": CPEm,
            "PaisEm": PaisEm,
            "ContactoEm": ContactoEm,
            "EmailEm": EmailEm,
            "TelefonoEm": TelefonoEm,
            "CIFCliente": CIFCliente,
            "DireccionCliente": DireccionCliente,
            "PoblacionCliente": PoblacionCliente,
            "ProvinciaCliente": ProvinciaCliente,
            "CPCliente": CPCliente,
            "PaisCliente": PaisCliente,
            "ContactoCliente": ContactoCliente,
            "EmailCliente": EmailCliente,
            "TelefonoCliente": TelefonoCliente,
            "Concepto" : Concepto,
            "Precio" : Precio,
            "Unidades" : Unidades,
            "Importe bruto": ImporteBruto,
            "IVA": IVA,
            "Importe total": ImporteTotal
        }

        jinja = jinja2.get_jinja2(app = self.app)
        self.response.write(jinja.render_template("answer.html", **valores_plantilla))

app = webapp2.WSGIApplication([
    ('/entrega2', MainHandler)
], debug=True)
