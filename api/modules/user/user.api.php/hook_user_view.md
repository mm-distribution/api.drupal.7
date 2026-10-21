# hook_user_view()

- **Type:** Hook (documentation function)
- **File:** [`modules/user/user.api.php`](_file.md), lines 356–365 · [local source](../../../../source/modules/user/user.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php#L356-L365)
- **Module/theme:** user
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_user_view($account, $view_mode, $langcode)
```

## Documentation

```text
The user's account information is being displayed.

The module should format its custom additions for display and add them to the
$account->content array.

@param $account
  The user object on which the operation is being performed.
@param $view_mode
  View mode, e.g. 'full'.
@param $langcode
  The language code used for rendering.

@see hook_user_view_alter()
@see hook_entity_view()
```

## Code

```php
function hook_user_view($account, $view_mode, $langcode) {
  if (user_access('create blog content', $account)) {
    $account->content['summary']['blog'] =  array(
      '#type' => 'user_profile_item',
      '#title' => t('Blog'),
      '#markup' => l(t('View recent blog entries'), "blog/$account->uid", array('attributes' => array('title' => t("Read !username's latest blog entries.", array('!username' => format_username($account)))))),
      '#attributes' => array('class' => array('blog')),
    );
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_user_view()".

- [blog_user_view()](../../blog/blog.module/blog_user_view.md) — `modules/blog/blog.module`
- [profile_user_view()](../../profile/profile.module/profile_user_view.md) — `modules/profile/profile.module`
- [trigger_user_view()](../../trigger/trigger.module/trigger_user_view.md) — `modules/trigger/trigger.module`
- [user_user_view()](../user.module/user_user_view.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/user/user.api.php](https://github.com/drupal/drupal/blob/7.103/modules/user/user.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
