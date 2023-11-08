import random

import pytest
import inspect

import analyzer.model.adn

module_members = [item[0] for item in inspect.getmembers(analyzer.model.adn)]
condition_defined = 'Condition' in module_members
length_condition_defined = 'LengthCondition' in module_members
gc_content_condition_defined = 'GCContentCondition' in module_members
atg_presence_condition_defined = 'ATGPresenceCondition' in module_members
cta_presence_condition_defined = 'CTAPresenceCondition' in module_members
adn_analyzer_defined = 'ADNAnalyzer' in module_members

if condition_defined:
    from analyzer.model.adn import Condition

if length_condition_defined:
    from analyzer.model.adn import LengthCondition

if gc_content_condition_defined:
    from analyzer.model.adn import GCContentCondition

if atg_presence_condition_defined:
    from analyzer.model.adn import ATGPresenceCondition

if cta_presence_condition_defined:
    from analyzer.model.adn import CTAPresenceCondition

if adn_analyzer_defined:
    from analyzer.model.adn import ADNAnalyzer


@pytest.fixture
def length_condition():
    return LengthCondition(50)


@pytest.fixture
def gc_content_condition():
    return GCContentCondition(60)


@pytest.fixture
def atg_presence_condition():
    return ATGPresenceCondition()


@pytest.fixture
def cta_presence_condition():
    return CTAPresenceCondition()


@pytest.fixture
def adn_analyzer_without_conditions():
    return ADNAnalyzer("data/good_data.txt")


@pytest.fixture
def adn_analyzer_with_conditions_and_perfect_data():
    adn_analyzer = ADNAnalyzer("data/perfect_adn_data.txt")
    adn_analyzer.add_condition(LengthCondition(50))
    adn_analyzer.add_condition(GCContentCondition(60))
    adn_analyzer.add_condition(ATGPresenceCondition())
    adn_analyzer.add_condition(CTAPresenceCondition())
    return adn_analyzer


@pytest.fixture
def adn_analyzer_with_conditions_and_good_data():
    adn_analyzer = ADNAnalyzer("data/good_data.txt")
    adn_analyzer.add_condition(LengthCondition(50))
    adn_analyzer.add_condition(GCContentCondition(60))
    adn_analyzer.add_condition(ATGPresenceCondition())
    adn_analyzer.add_condition(CTAPresenceCondition())
    return adn_analyzer


@pytest.fixture
def adn_analyzer_with_conditions_and_regular_data():
    adn_analyzer = ADNAnalyzer("data/regular_data.txt")
    adn_analyzer.add_condition(LengthCondition(50))
    adn_analyzer.add_condition(GCContentCondition(60))
    adn_analyzer.add_condition(ATGPresenceCondition())
    adn_analyzer.add_condition(CTAPresenceCondition())
    return adn_analyzer


@pytest.fixture
def adn_analyzer_with_conditions_and_no_satisfactory_data():
    adn_analyzer = ADNAnalyzer("data/no_satisfactory_data.txt")
    adn_analyzer.add_condition(LengthCondition(50))
    adn_analyzer.add_condition(GCContentCondition(60))
    adn_analyzer.add_condition(ATGPresenceCondition())
    adn_analyzer.add_condition(CTAPresenceCondition())
    return adn_analyzer


@pytest.fixture
def adn_analyzer_with_conditions_and_invalid_data():
    adn_analyzer = ADNAnalyzer("data/invalid_data.txt")
    adn_analyzer.add_condition(LengthCondition(50))
    adn_analyzer.add_condition(GCContentCondition(60))
    adn_analyzer.add_condition(ATGPresenceCondition())
    adn_analyzer.add_condition(CTAPresenceCondition())
    return adn_analyzer


@pytest.fixture
def perfect_adn_sequence():
    return "ATG" + "".join([random.choice("CG") for _ in range(50)]) + "CTA" * 3


def test_clase_Condition_es_abstracta():
    assert inspect.isabstract(Condition)


@pytest.mark.xfail(not (condition_defined or length_condition_defined), reason="required classes not defined")
def test_clase_LengthCondition_hereda_de_Condition():
    assert issubclass(LengthCondition, Condition)


@pytest.mark.xfail(not (condition_defined or gc_content_condition_defined), reason="required classes not defined")
def test_clase_GCContentCondition_hereda_de_Condition():
    assert issubclass(GCContentCondition, Condition)


@pytest.mark.xfail(not (condition_defined or atg_presence_condition_defined), reason="required classes not defined")
def test_clase_ATGPresenceCondition_hereda_de_Condition():
    assert issubclass(ATGPresenceCondition, Condition)


@pytest.mark.xfail(not (condition_defined or cta_presence_condition_defined), reason="required classes not defined")
def test_clase_CTAPresenceCondition_hereda_de_Condition():
    assert issubclass(CTAPresenceCondition, Condition)


@pytest.mark.xfail(not adn_analyzer_defined, reason="required classes not defined")
@pytest.mark.parametrize("method", ["__init__", "analyze", "add_condition", "_evaluate_conditions", "_validate_sequence"])
def test_clase_ADNAnalyzer_tiene_metodos(method):
    assert hasattr(ADNAnalyzer, method)


@pytest.mark.xfail(not length_condition_defined, reason="required classes not defined")
@pytest.mark.parametrize("method", ["__init__", "evaluate"])
def test_clase_LengthCondition_tiene_metodos(method):
    assert hasattr(LengthCondition, method)


@pytest.mark.xfail(not gc_content_condition_defined, reason="required classes not defined")
@pytest.mark.parametrize("method", ["__init__", "evaluate"])
def test_clase_GCContentCondition_tiene_metodos(method):
    assert hasattr(GCContentCondition, method)


@pytest.mark.xfail(not atg_presence_condition_defined, reason="required classes not defined")
@pytest.mark.parametrize("method", ["__init__", "evaluate"])
def test_clase_ATGPresenceCondition_tiene_metodos(method):
    assert hasattr(ATGPresenceCondition, method)


@pytest.mark.xfail(not cta_presence_condition_defined, reason="required classes not defined")
@pytest.mark.parametrize("method", ["__init__", "evaluate"])
def test_clase_CTAPresentCondition_tiene_metodos(method):
    assert hasattr(CTAPresenceCondition, method)


@pytest.mark.xfail(not length_condition_defined, reason="required classes not defined")
def test_clase_LengthCondition_tiene_atributo_min_length():
    assert hasattr(LengthCondition(), "min_length")


@pytest.mark.xfail(not gc_content_condition_defined, reason="required classes not defined")
def test_clase_GCContentCondition_tiene_atributo_min_gc_content():
    assert hasattr(GCContentCondition(), "min_gc_content")


@pytest.mark.xfail(not adn_analyzer_defined, reason="required classes not defined")
@pytest.mark.parametrize("attribute", ["conditions", "data_file"])
def test_clase_ADNAnalyzer_tiene_atributos(attribute):
    assert hasattr(ADNAnalyzer(""), attribute)


@pytest.mark.xfail(not adn_analyzer_defined, reason="required classes not defined")
def test_metodo_validate_sequence_es_estatico():
    assert inspect.isfunction(ADNAnalyzer._validate_sequence)


@pytest.mark.xfail(not (condition_defined and length_condition_defined), reason="required classes not defined")
@pytest.mark.parametrize("min_length, sequence, expected", [
    (50, "ATG" + "".join([random.choice("CG") for _ in range(50)]) + "CTA" * 3, True),
    (50, "ATG" + "".join([random.choice("CG") for _ in range(30)]) + "CTA" * 3, False),
    (50, "ATG" + "".join([random.choice("CG") for _ in range(51)]) + "CTA" * 3, True),
    (50, "ATG" + "".join([random.choice("CG") for _ in range(30)]) + "CTA" * 2, False)])
def test_clase_LengthCondition_evaluate_retorna_valor_esperado(length_condition, min_length, sequence, expected):
    length_condition.min_length = min_length
    assert length_condition.evaluate(sequence) == expected


@pytest.mark.xfail(not (condition_defined and gc_content_condition_defined), reason="required classes not defined")
@pytest.mark.parametrize("min_gc_content, sequence, expected", [
    (60, "ATG" + "".join([random.choice("CG") for _ in range(50)]) + "CTA" * 3, True),
    (60, "ATG" + "".join([random.choice("CG") for _ in range(10)]) + "CTA" * 20, False),
    (60, "ATG" + "".join([random.choice("CG") for _ in range(51)]) + "CTA" * 3, True),
    (60, "ATG" + "".join([random.choice("CG") for _ in range(20)]) + "CTA" * 20, False)])
def test_clase_GCContentCondition_evaluate_retorna_valor_esperado(gc_content_condition, min_gc_content, sequence,
                                                                  expected):
    gc_content_condition.min_gc_content = min_gc_content
    assert gc_content_condition.evaluate(sequence) == expected


@pytest.mark.xfail(not (condition_defined and atg_presence_condition_defined), reason="required classes not defined")
@pytest.mark.parametrize("sequence, expected", [
    ("ATG" + "".join([random.choice("CG") for _ in range(50)]) + "CTA" * 3, True),
    ("A" + "".join([random.choice("CG") for _ in range(49)]) + "CTA" * 3, False),
    ("ATG" + "".join([random.choice("CG") for _ in range(51)]) + "CTA" * 3, True),
    ("AG" + "".join([random.choice("CG") for _ in range(50)]) + "CTA" * 2, False)])
def test_clase_ATGPresenceCondition_evaluate_retorna_valor_esperado(atg_presence_condition, sequence, expected):
    assert atg_presence_condition.evaluate(sequence) == expected


@pytest.mark.xfail(not (condition_defined and cta_presence_condition_defined), reason="required classes not defined")
@pytest.mark.parametrize("sequence, expected", [
    ("ATG" + "".join([random.choice("CG") for _ in range(50)]) + "CTA" * 3, True),
    ("A" + "".join([random.choice("CG") for _ in range(49)]) + "CTA" * 2, False),
    ("ATG" + "".join([random.choice("CG") for _ in range(51)]) + "CTA" * 3, True),
    ("AG" + "".join([random.choice("CG") for _ in range(50)]) + "CTA" * 2, False)])
def test_clase_CTAPresenceCondition_evaluate_retorna_valor_esperado(cta_presence_condition, sequence, expected):
    assert cta_presence_condition.evaluate(sequence) == expected


@pytest.mark.xfail(not adn_analyzer_defined, reason="required classes not defined")
def test_ADNAnalyzer_no_tiene_condiciones_por_defecto(adn_analyzer_without_conditions):
    assert len(adn_analyzer_without_conditions.conditions) == 0


@pytest.mark.xfail(not adn_analyzer_defined, reason="required classes not defined")
def test_ADNAnalyzer_tiene_condiciones_despues_de_agregarlas(adn_analyzer_without_conditions):
    adn_analyzer_without_conditions.add_condition(LengthCondition(50))
    adn_analyzer_without_conditions.add_condition(GCContentCondition(60))
    adn_analyzer_without_conditions.add_condition(ATGPresenceCondition())
    adn_analyzer_without_conditions.add_condition(CTAPresenceCondition())
    assert len(adn_analyzer_without_conditions.conditions) == 4


@pytest.mark.xfail(not adn_analyzer_defined, reason="required classes not defined")
@pytest.mark.parametrize("sequence, expected", [
    ("ATGGGGCGGGGCCCCGGGCGCGCGCGGGGGGGGCCGCGGCGCCGCCCCCCGGCCTACTACTA", "ADN perfecto, posible forma de vida"),
    ("ATG" + "".join([random.choice("CG") for _ in range(60)]) + "CTA" * 2, "ADN bueno"),
    ("AG" + "".join([random.choice("CG") for _ in range(50)]) + "CTA" * 2, "ADN regular"),
    ("A" + "".join([random.choice("CG") for _ in range(30)]) + "CTA" * 2, "ADN no satisfactorio")])
def test_ADNAnalyzer_evaluate_condition_retorna_valor_esperado(adn_analyzer_with_conditions_and_good_data,
                                                               sequence, expected):
    assert adn_analyzer_with_conditions_and_good_data._evaluate_conditions(sequence) == expected


@pytest.mark.xfail(not adn_analyzer_defined, reason="required classes not defined")
def test_ADNAnalyzer_analyze_retorna_mensaje_esperado_para_adn_perfecto(adn_analyzer_with_conditions_and_perfect_data):
    expected = {"Organismo 1": "ADN perfecto, posible forma de vida"}
    assert adn_analyzer_with_conditions_and_perfect_data.analyze() == expected


@pytest.mark.xfail(not adn_analyzer_defined, reason="required classes not defined")
def test_ADNAnalyzer_analyze_retorna_mensaje_esperado_para_adn_bueno(adn_analyzer_with_conditions_and_good_data):
    expected = {"Organismo 1": "ADN bueno"}
    assert adn_analyzer_with_conditions_and_good_data.analyze() == expected


@pytest.mark.xfail(not adn_analyzer_defined, reason="required classes not defined")
def test_ADNAnalyzer_analyze_retorna_mensaje_esperado_para_adn_regular(adn_analyzer_with_conditions_and_regular_data):
    expected = {"Organismo 1": "ADN regular"}
    assert adn_analyzer_with_conditions_and_regular_data.analyze() == expected


@pytest.mark.xfail(not adn_analyzer_defined, reason="required classes not defined")
def test_ADNAnalyzer_analyze_retorna_mensaje_esperado_para_adn_no_satisfactorio(
        adn_analyzer_with_conditions_and_no_satisfactory_data):
    expected = {"Organismo 1": "ADN no satisfactorio", "Organismo 2": "ADN no satisfactorio"}
    assert adn_analyzer_with_conditions_and_no_satisfactory_data.analyze() == expected


@pytest.mark.xfail(not adn_analyzer_defined, reason="required classes not defined")
@pytest.mark.parametrize("sequence, expected", [
    ("ATG" + "".join([random.choice("CG") for _ in range(50)]) + "CTA" * 3, True),
    ("A" + "".join([random.choice("CX") for _ in range(49)]) + "CTA" * 2, False),
    ("ATZ" + "".join([random.choice("CG") for _ in range(51)]) + "CTA" * 3, False),
    ("AG" + "".join([random.choice("CG") for _ in range(50)]) + "CTA" * 2, True)])
def test_ADNAnalyzer_validate_sequence_retorna_valor_esperado_para_secuencia(adn_analyzer_without_conditions, sequence,
                                                                             expected):
    assert adn_analyzer_without_conditions._validate_sequence(sequence) == expected


@pytest.mark.xfail(not adn_analyzer_defined, reason="required classes not defined")
def test_ADNAnalyzer_arroja_excepcion_si_datos_no_son_validos(adn_analyzer_with_conditions_and_invalid_data):
    with pytest.raises(ValueError):
        adn_analyzer_with_conditions_and_invalid_data.analyze()