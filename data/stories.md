## happy path
* greet
  - utter_greet
* affirm
  - IMC_form
  - form{"name":"IMC_form"}
  - form{"name":null}
* thankyou
  - utter_thanks
  
## early stopping
* greet
  - utter_greet
* deny
  - utter_confirmation
* affirm
  - utter_goodbye

## early stopping feint
* greet
  - utter_greet
* deny
  - utter_confirmation
* deny
  - IMC_form
  - form{"name": "IMC_form"}
  - form{"name": null}
* thankyou
  - utter_thanks

## stop but continue path
* greet
  - utter_greet
* affirm
  - IMC_form
  - form{"name": "IMC_form"}
* deny
  - utter_confirmation
* deny
  - IMC_form
  - form{"name": null}
* thankyou
  - utter_thanks

## stop and really stop path
* greet
  - utter_greet
* affirm
  - IMC_form
  - form{"name": "IMC_form"}
* deny
  - utter_confirmation
* affirm
  - action_deactivate_form
  - form{"name": null}
  - utter_goodbye

## diverge but continue path
* greet
  - utter_greet
* affirm
  - IMC_form
  - form{"name": "IMC_form"}
* out_of_scope
  - utter_outscope
  - utter_continuation
* affirm
  - IMC_form
  - form{"name": null}
* thankyou
  - utter_thanks  

## diverge but stop path
* greet
  - utter_greet
* affirm
  - IMC_form
  - form{"name": "IMC_form"}
* out_of_scope
  - utter_outscope
  - utter_continuation
* deny
  - action_deactivate_form
  - form{"name": null}
  - utter_goodbye
