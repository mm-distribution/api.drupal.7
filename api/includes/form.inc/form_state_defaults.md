# form_state_defaults()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 402–423 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L402-L423)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_state_defaults()
```

## Documentation

```text
Retrieves default values for the $form_state array.
```

## Code

```php
function form_state_defaults() {
  return array(
    'rebuild' => FALSE,
    'rebuild_info' => array(),
    'redirect' => NULL,
    // @todo 'args' is usually set, so no other default 'build_info' keys are
    //   appended via += form_state_defaults().
    'build_info' => array(
      'args' => array(),
      'files' => array(),
    ),
    'temporary' => array(),
    'submitted' => FALSE,
    'executed' => FALSE,
    'programmed' => FALSE,
    'programmed_bypass_access_check' => TRUE,
    'cache'=> FALSE,
    'method' => 'post',
    'groups' => array(),
    'buttons' => array(),
  );
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
