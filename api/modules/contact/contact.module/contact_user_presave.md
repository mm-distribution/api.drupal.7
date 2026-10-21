# contact_user_presave()

- **Type:** Function
- **File:** [`modules/contact/contact.module`](_file.md), lines 236–245 · [local source](../../../../source/modules/contact/contact.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module#L236-L245)
- **Module/theme:** contact
- **Implements:** [hook_user_presave()](../../user/user.api.php/hook_user_presave.md)

## Signature

```php
function contact_user_presave(&$edit, $account, $category)
```

## Documentation

```text
Implements hook_user_presave().
```

## Code

```php
function contact_user_presave(&$edit, $account, $category) {
  if (isset($edit['contact'])) {
    // Set new value.
    $edit['data']['contact'] = $edit['contact'];
  }
  elseif (!isset($account->data['contact'])) {
    // Use default if none has been set.
    $edit['data']['contact'] = variable_get('contact_default_status', 1);
  }
}
```

---
_Drupal 7.103 · [modules/contact/contact.module](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module) · Licensed GPL-2.0-or-later (see LICENSE)._
