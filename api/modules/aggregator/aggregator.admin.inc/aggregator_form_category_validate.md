# aggregator_form_category_validate()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.admin.inc`](_file.md), lines 575–588 · [local source](../../../../source/modules/aggregator/aggregator.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc#L575-L588)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_form_category_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for aggregator_form_category().

@see aggregator_form_category_submit()
```

## Code

```php
function aggregator_form_category_validate($form, &$form_state) {
  if ($form_state['values']['op'] == t('Save')) {
    // Check for duplicate titles
    if (isset($form_state['values']['cid'])) {
      $category = db_query("SELECT cid FROM {aggregator_category} WHERE title = :title AND cid <> :cid", array(':title' => $form_state['values']['title'], ':cid' => $form_state['values']['cid']))->fetchObject();
    }
    else {
      $category = db_query("SELECT cid FROM {aggregator_category} WHERE title = :title", array(':title' => $form_state['values']['title']))->fetchObject();
    }
    if ($category) {
      form_set_error('title', t('A category named %category already exists. Enter a unique title.', array('%category' => $form_state['values']['title'])));
    }
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
