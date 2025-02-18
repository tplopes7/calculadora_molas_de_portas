class SpringForceCalculator:
    def __init__(self, attributes):
        self.attributes = attributes

    def get_attribute_value(self, attribute_id):
        for attribute in self.attributes:
            if attribute['ID'] == attribute_id:
                return attribute['Values']['DataElementList'][0]['Value']
        return None

    def calculate_door_weight(self):
        door_width = float(self.get_attribute_value('DOORWIDTH'))
        door_height = float(self.get_attribute_value('DOORHEIGHT'))
        calculation_weight = float(self.get_attribute_value('CALCULATIONWEIGHT'))
        door_weight = door_width * door_height * calculation_weight
        return door_weight

    def calculate_spring_force(self):
        cycle_count = float(self.get_attribute_value('CYCLECOUNT'))
        calculation_weight = float(self.get_attribute_value('CALCULATIONWEIGHT'))
        spring_force = cycle_count * calculation_weight
        return spring_force

    def calculate_cable_strength(self):
        cable_diameter = float(self.get_attribute_value('CABLEDIAMETER'))
        cable_max_load = float(self.get_attribute_value('CABLEMAXLOAD'))
        cable_strength = cable_diameter * cable_max_load
        return cable_strength

    def display_specifications(self):
        print(f"Largura da Porta: {self.get_attribute_value('DOORWIDTH')} mm")
        print(f"Altura da Porta: {self.get_attribute_value('DOORHEIGHT')} mm")
        print(f"Peso da Porta: {self.calculate_door_weight()} kg")
        print(f"Força da Mola: {self.calculate_spring_force()} N")
        print(f"Diâmetro do Cabo: {self.get_attribute_value('CABLEDIAMETER')} mm")
        print(f"Força Máxima do Cabo: {self.calculate_cable_strength()} N")

# Exemplo de uso do programa
attributes = [
    {"ID": "DOORWIDTH", "Values": {"DataElementList": [{"Value": "3000"}]}},
    {"ID": "DOORHEIGHT", "Values": {"DataElementList": [{"Value": "2500"}]}},
    {"ID": "CALCULATIONWEIGHT", "Values": {"DataElementList": [{"Value": "12"}]}},
    {"ID": "CYCLECOUNT", "Values": {"DataElementList": [{"Value": "15000"}]}},
    {"ID": "CABLEDIAMETER", "Values": {"DataElementList": [{"Value": "3"}]}},
    {"ID": "CABLEMAXLOAD", "Values": {"DataElementList": [{"Value": "163"}]}}
]

calculator = SpringForceCalculator(attributes)
calculator.display_specifications()