# -*- coding: utf-8 -*-
##############################################################################
#
#    Soltic SRL
#    Copyright (C) 2011 Soltic SRL (<http://www.soltic.com.ar>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import fields, osv
from openerp import tools
import time
from datetime import datetime
import calendar
from openerp.tools.translate import _

class medical_diagnostic_view(osv.osv):
    _name = 'medical.diagnostic.view'
    _auto = False
    _order = 'appointment_date desc'

    

    _columns = {
    	# 'doctor_id': fields.many2one('res.partner', 'Especialista', readonly=True),
    	'patient_id': fields.many2one('res.partner', 'Afiliado', readonly=True),
    	# 'f_fecha_practica': fields.date('Fecha Atención', readonly=True),
        'appointment_date': fields.date('Fecha', readonly=True),
        # 'practice_id': fields.many2one('medical.practice', 'Práctica Realizada', readonly=True),
        'diagnostic_id': fields.many2one('medical.diagnostic', 'Diagnóstico', readonly=True),
        'symptom': fields.char('Síntomas', readonly=True),
        'attention_city_id': fields.many2one('res.department.city', 'Cuidad de Atención', readonly=True),
        'attention_department_id': fields.many2one('res.state.department', 'Departamento', readonly=True),
        'sex' : fields.selection([('M', 'Masculino'),('F', 'Femenino'),], 'Sex', select=True),
        'age': fields.integer('Edad'),
    	'care_type': fields.selection([
            ('1','Atención Programada a Domicilio'),
            ('2','Urgencias en Domicilio'),
            ('3','Atención telefónica'),
            ('4', 'Consultorio Externo'),
            ('5', 'Hospital de Dia Jornada Simple'),
            ('6', 'Hospital de Dia Jornada Completa'),
            ('7', 'Atención en Jurisdicciónes Alejadas'),
        ], 'Tipo de Atención'), ##---- Tipo de atencion 
        'm_tipo_diagnostico': fields.selection([('1','Principal'),('2','Secundario')],'Tipo de Diagnóstico', readonly=True),
        'year': fields.char('Período')
    }

    def init(self, cr):
      tools.drop_view_if_exists(cr, 'medical_diagnostic_view')
      cr.execute("""
            CREATE OR REPLACE VIEW medical_diagnostic_view AS
                select mad.id, ma.patient as patient_id, --map.f_fecha_practica, map.practice_id, map.doctor_id, 
                mad.diagnostic_id, ma.symptom, mad.m_tipo_diagnostico,
                    pat.attention_city_id, pat.attention_department_id, pat.sex, extract(year from age(pat.dob)) as age, ma.care_type, ma.appointment_date,
                    left(appointment_date::text,7) as year
                from --medical_appointment_practice map join 
                medical_appointment ma --on (map.appointment_id=ma.id)
                join medical_appointment_diagnostic mad on (mad.appointment_id=ma.id)
                join res_partner pat on (ma.patient=pat.id)

            """)

medical_diagnostic_view()  