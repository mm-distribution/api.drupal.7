# path_admin_form_delete_submit()

- **Type:** Function
- **File:** [`modules/path/path.admin.inc`](_file.md), lines 181–188 · [local source](../../../../source/modules/path/path.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc#L181-L188)
- **Module/theme:** path

## Signature

```php
function path_admin_form_delete_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for the 'Delete' button on path_admin_form().

@see path_admin_form_validate()
@see path_admin_form_submit()
```

## Code

```php
function path_admin_form_delete_submit($form, &$form_state) {
  $destination = array();
  if (isset($_GET['destination'])) {
    $destination = drupal_get_destination();
    unset($_GET['destination']);
  }
  $form_state['redirect'] = array('admin/config/search/path/delete/' . $form_state['values']['pid'], array('query' => $destination));
}
```

---
_Drupal 7.103 · [modules/path/path.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
