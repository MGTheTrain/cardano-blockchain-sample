from opshin.prelude import *

@dataclass()
class HealthDatum(PlutusData):
    patient_id: bytes
    doctor_id: bytes
    diagnosis: str
    treatment: str
    cost: int

def validator(datum: HealthDatum, redeemer: None, context: ScriptContext) -> None:
    assert datum.cost > 0, "Cost must be greater than zero"
    assert len(datum.patient_id) == 32, "Invalid patient ID"
    assert len(datum.doctor_id) == 32, "Invalid doctor ID"