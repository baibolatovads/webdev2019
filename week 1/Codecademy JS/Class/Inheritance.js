class HospitalEmployee{
  constructor(name, remainingVacationDays){
		this._name = name;
    this._remainingVacationDays = 20;
  }
  get name(){
			return this._name;
  }
  get remainingVacationDays(){
    return this._remainingVacationDays;
  }
  takeVacationDays(daysOff){
    this._remainingVacationDays -= daysOff;
  }
}