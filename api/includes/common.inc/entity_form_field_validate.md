# entity_form_field_validate()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8466–8474 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8466-L8474)

## Signature

```php
function entity_form_field_validate($entity_type, $form, &$form_state)
```

## Documentation

```text
Attaches field API validation to entity forms.
```

## Code

```php
function entity_form_field_validate($entity_type, $form, &$form_state) {
  // All field attach API functions act on an entity object, but during form
  // validation, we don't have one. $form_state contains the entity as it was
  // prior to processing the current form submission, and we must not update it
  // until we have fully validated the submitted input. Therefore, for
  // validation, act on a pseudo entity created out of the form values.
  $pseudo_entity = (object) $form_state['values'];
  field_attach_form_validate($entity_type, $pseudo_entity, $form, $form_state);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
