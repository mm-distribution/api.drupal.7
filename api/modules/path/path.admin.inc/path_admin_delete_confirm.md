# path_admin_delete_confirm()

- **Type:** Function
- **File:** [`modules/path/path.admin.inc`](_file.md), lines 243–254 · [local source](../../../../source/modules/path/path.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc#L243-L254)
- **Module/theme:** path

## Signature

```php
function path_admin_delete_confirm($form, &$form_state, $path)
```

## Documentation

```text
Form constructor for the path deletion form.

@param $path
  The path alias that will be deleted.

@see path_admin_delete_confirm_submit()
```

## Code

```php
function path_admin_delete_confirm($form, &$form_state, $path) {
  if (user_access('administer url aliases')) {
    $form_state['path'] = $path;
    return confirm_form(
      $form,
      t('Are you sure you want to delete path alias %title?',
      array('%title' => $path['alias'])),
      'admin/config/search/path'
    );
  }
  return array();
}
```

---
_Drupal 7.103 · [modules/path/path.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
