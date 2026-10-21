# profile_help()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 31–50 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L31-L50)
- **Module/theme:** profile
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function profile_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function profile_help($path, $arg) {
  switch ($path) {
    case 'admin/help#profile':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Profile module allows site administrators to define custom fields (such as country, full name, or age) for user profiles, which are then displayed in the <a href="@user">My Account</a> section. This permits users of a site to share more information about themselves, and can help community-based sites organize users around specific information. For more information, see the online handbook entry for <a href="@profile">Profile module</a>.', array('@user' => url('user'), '@profile' => 'http://drupal.org/documentation/modules/profile/')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Adding fields to the default profile') . '</dt>';
      $output .= '<dd>' . t('To provide the ability for users to enter more information about themselves, the Profile module allows additional fields to be added to the default user profile. Examples of common additions would be <em>Location</em>, <em>Company</em>, <em>Age</em>, or <em>About me</em>.') . '</dd>';
      $output .= '<dt>' . t('User information pages') . '</dt>';
      $output .= '<dd>' . t('The Profile module enables links to see further information about site users. You can view both a main <a href="@profile">User list page</a>, and more specified pages by clicking on linked fields in any profile. For example, the <a href="@profile-country">People who live in Canada</a> listing on Drupal.org displays all users who have entered <em>Canada</em> in the <em>Country</em> field on their user profile.', array('@profile' => url('profile'), '@profile-country' => 'http://drupal.org/profile/country/Canada')) . '</dd>';
      $output .= '<dt>' . t('Author information block') . '</dt>';
      $output .= '<dd>' . t('The <em>Author information block</em> is a default block created by the Profile module that can be enabled on the <a href="@blocks">Blocks administration page</a>. It shows visitors of your website information about the author of the page they are reading.', array('@blocks' => url('admin/structure/block'))) . '</dd>';
      $output .= '</dl>';
      return $output;
    case 'admin/config/people/profile':
      return '<p>' . t("This page displays a list of the existing custom profile fields to be displayed on a user's <em>My account</em> page. To provide structure, similar or related fields may be placed inside a category. To add a new category (or edit an existing one), edit a profile field and provide a new category name.") . '</p>';
  }
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
