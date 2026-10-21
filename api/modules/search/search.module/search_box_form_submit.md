# search_box_form_submit()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 1028–1055 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L1028-L1055)
- **Module/theme:** search
- **Topics:** [search](../../../topics/search.md)

## Signature

```php
function search_box_form_submit($form, &$form_state)
```

## Documentation

```text
Process a block search form submission.
```

## Code

```php
function search_box_form_submit($form, &$form_state) {
  // The search form relies on control of the redirect destination for its
  // functionality, so we override any static destination set in the request,
  // for example by drupal_access_denied() or drupal_not_found()
  // (see http://drupal.org/node/292565).
  if (isset($_GET['destination'])) {
    unset($_GET['destination']);
  }

  // Check to see if the form was submitted empty.
  // If it is empty, display an error message.
  // (This method is used instead of setting #required to TRUE for this field
  // because that results in a confusing error message.  It would say a plain
  // "field is required" because the search keywords field has no title.
  // The error message would also complain about a missing #title field.)
  if ($form_state['values']['search_block_form'] == '') {
    form_set_error('keys', t('Please enter some keywords.'));
  }

  $form_id = $form['form_id']['#value'];
  $info = search_get_default_module_info();
  if ($info) {
    $form_state['redirect'] = 'search/' . $info['path'] . '/' . trim($form_state['values'][$form_id]);
  }
  else {
    form_set_error(NULL, t('Search is currently disabled.'), 'error');
  }
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
