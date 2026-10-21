# aggregator_form_opml_validate()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.admin.inc`](_file.md), lines 302–312 · [local source](../../../../source/modules/aggregator/aggregator.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc#L302-L312)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_form_opml_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for aggregator_form_opml().

@see aggregator_form_opml_submit()
```

## Code

```php
function aggregator_form_opml_validate($form, &$form_state) {
  // If both fields are empty or filled, cancel.
  if (empty($form_state['values']['remote']) == empty($_FILES['files']['name']['upload'])) {
    form_set_error('remote', t('You must <em>either</em> upload a file or enter a URL.'));
  }

  // Validate the URL, if one was entered.
  if (!empty($form_state['values']['remote']) && !valid_url($form_state['values']['remote'], TRUE)) {
    form_set_error('remote', t('This URL is not valid.'));
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
