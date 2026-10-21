# hook_user_categories()

- **Type:** Hook (documentation function)
- **File:** [`modules/user/user.api.php`](_file.md), lines 216–222 · [local source](../../../../source/modules/user/user.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php#L216-L222)
- **Module/theme:** user
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_user_categories()
```

## Documentation

```text
Define a list of user settings or profile information categories.

There are two steps to using hook_user_categories():
- Create the category with hook_user_categories().
- Display that category on the form ID of "user_profile_form" with
  hook_form_FORM_ID_alter().

Step one builds out the category but it won't be visible on your form until
you explicitly tell it to do so.

The function in step two should contain the following code in order to
display your new category:
@code
if ($form['#user_category'] == 'mycategory') {
  // Return your form here.
}
@endcode

@return
  An array of associative arrays. Each inner array has elements:
  - "name": The internal name of the category.
  - "title": The human-readable, localized name of the category.
  - "weight": An integer specifying the category's sort ordering.
  - "access callback": Name of the access callback function to use to
    determine whether the user can edit the category. Defaults to using
    user_edit_access(). See hook_menu() for more information on access
    callbacks.
  - "access arguments": Arguments for the access callback function. Defaults
    to array(1).
```

## Code

```php
function hook_user_categories() {
  return array(array(
    'name' => 'account',
    'title' => t('Account settings'),
    'weight' => 1,
  ));
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_user_categories()".

- [profile_user_categories()](../../profile/profile.module/profile_user_categories.md) — `modules/profile/profile.module`
- [user_user_categories()](../user.module/user_user_categories.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/user/user.api.php](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
