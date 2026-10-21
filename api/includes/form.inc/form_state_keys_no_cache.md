# form_state_keys_no_cache()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 593–617 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L593-L617)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_state_keys_no_cache()
```

## Documentation

```text
Returns an array of $form_state keys that shouldn't be cached.
```

## Code

```php
function form_state_keys_no_cache() {
  return array(
    // Public properties defined by form constructors and form handlers.
    'always_process',
    'must_validate',
    'rebuild',
    'rebuild_info',
    'redirect',
    'no_redirect',
    'temporary',
    // Internal properties defined by form processing.
    'buttons',
    'triggering_element',
    'clicked_button',
    'complete form',
    'groups',
    'input',
    'method',
    'submit_handlers',
    'submitted',
    'executed',
    'validate_handlers',
    'values',
  );
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
