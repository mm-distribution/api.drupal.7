# hook_user_cancel_methods_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/user/user.api.php`](_file.md), lines 135–149 · [local source](../../../../source/modules/user/user.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php#L135-L149)
- **Module/theme:** user
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_user_cancel_methods_alter(&$methods)
```

## Documentation

```text
Modify account cancellation methods.

By implementing this hook, modules are able to add, customize, or remove
account cancellation methods. All defined methods are turned into radio
button form elements by user_cancel_methods() after this hook is invoked.
The following properties can be defined for each method:
- title: The radio button's title.
- description: (optional) A description to display on the confirmation form
  if the user is not allowed to select the account cancellation method. The
  description is NOT used for the radio button, but instead should provide
  additional explanation to the user seeking to cancel their account.
- access: (optional) A boolean value indicating whether the user can access
  a method. If access is defined, the method cannot be configured as the
  default method.

@param $methods
  An array containing user account cancellation methods, keyed by method id.

@see user_cancel_methods()
@see user_cancel_confirm_form()
```

## Code

```php
function hook_user_cancel_methods_alter(&$methods) {
  // Limit access to disable account and unpublish content method.
  $methods['user_cancel_block_unpublish']['access'] = user_access('administer site configuration');

  // Remove the content re-assigning method.
  unset($methods['user_cancel_reassign']);

  // Add a custom zero-out method.
  $methods['mymodule_zero_out'] = array(
    'title' => t('Delete the account and remove all content.'),
    'description' => t('All your content will be replaced by empty strings.'),
    // access should be used for administrative methods only.
    'access' => user_access('access zero-out account cancellation method'),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_user_cancel_methods_alter()".

_None found._

---
_Drupal 7.103 · [modules/user/user.api.php](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
