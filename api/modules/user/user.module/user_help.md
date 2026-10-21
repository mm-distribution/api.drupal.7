# user_help()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 37–74 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L37-L74)
- **Module/theme:** user
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function user_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function user_help($path, $arg) {
  global $user;

  switch ($path) {
    case 'admin/help#user':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The User module allows users to register, log in, and log out. It also allows users with proper permissions to manage user roles (used to classify users) and permissions associated with those roles. For more information, see the online handbook entry for <a href="@user">User module</a>.', array('@user' => 'http://drupal.org/documentation/modules/user')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Creating and managing users') . '</dt>';
      $output .= '<dd>' . t('The User module allows users with the appropriate <a href="@permissions">permissions</a> to create user accounts through the <a href="@people">People administration page</a>, where they can also assign users to one or more roles, and block or delete user accounts. If allowed, users without accounts (anonymous users) can create their own accounts on the <a href="@register">Create new account</a> page.', array('@permissions' => url('admin/people/permissions', array('fragment' => 'module-user')), '@people' => url('admin/people'), '@register' => url('user/register'))) . '</dd>';
      $output .= '<dt>' . t('User roles and permissions') . '</dt>';
      $output .= '<dd>' . t('<em>Roles</em> are used to group and classify users; each user can be assigned one or more roles. By default there are two roles: <em>anonymous user</em> (users that are not logged in) and <em>authenticated user</em> (users that are registered and logged in). Depending on choices you made when you installed Drupal, the installation process may have defined more roles, and you can create additional custom roles on the <a href="@roles">Roles page</a>. After creating roles, you can set permissions for each role on the <a href="@permissions_user">Permissions page</a>. Granting a permission allows users who have been assigned a particular role to perform an action on the site, such as viewing a particular type of content, editing or creating content, administering settings for a particular module, or using a particular function of the site (such as search).', array('@permissions_user' => url('admin/people/permissions'), '@roles' => url('admin/people/permissions/roles'))) . '</dd>';
      $output .= '<dt>' . t('Account settings') . '</dt>';
      $output .= '<dd>' . t('The <a href="@accounts">Account settings page</a> allows you to manage settings for the displayed name of the anonymous user role, personal contact forms, user registration, and account cancellation. On this page you can also manage settings for account personalization (including signatures and user pictures), and adapt the text for the e-mail messages that are sent automatically during the user registration process.', array('@accounts'  => url('admin/config/people/accounts'))) . '</dd>';
      $output .= '</dl>';
      return $output;
    case 'admin/people/create':
      return '<p>' . t("This web page allows administrators to register new users. Users' e-mail addresses and usernames must be unique.") . '</p>';
    case 'admin/people/permissions':
      return '<p>' . t('Permissions let you control what users can do and see on your site. You can define a specific set of permissions for each role. (See the <a href="@role">Roles</a> page to create a role). Two important roles to consider are Authenticated Users and Administrators. Any permissions granted to the Authenticated Users role will be given to any user who can log into your site. You can make any role the Administrator role for the site, meaning this will be granted all new permissions automatically. You can do this on the <a href="@settings">User Settings</a> page. You should be careful to ensure that only trusted users are given this access and level of control of your site.', array('@role' => url('admin/people/permissions/roles'), '@settings' => url('admin/config/people/accounts'))) . '</p>';
    case 'admin/people/permissions/roles':
      $output = '<p>' . t('Roles allow you to fine tune the security and administration of Drupal. A role defines a group of users that have certain privileges as defined on the <a href="@permissions">permissions page</a>. Examples of roles include: anonymous user, authenticated user, moderator, administrator and so on. In this area you will define the names and order of the roles on your site. It is recommended to order your roles from least permissive (anonymous user) to most permissive (administrator). To delete a role choose "edit role".', array('@permissions' => url('admin/people/permissions'))) . '</p>';
      $output .= '<p>' . t('By default, Drupal comes with two user roles:') . '</p>';
      $output .= '<ul>';
      $output .= '<li>' . t("Anonymous user: this role is used for users that don't have a user account or that are not authenticated.") . '</li>';
      $output .= '<li>' . t('Authenticated user: this role is automatically granted to all logged in users.') . '</li>';
      $output .= '</ul>';
      return $output;
    case 'admin/config/people/accounts/fields':
      return '<p>' . t('This form lets administrators add, edit, and arrange fields for storing user data.') . '</p>';
    case 'admin/config/people/accounts/display':
      return '<p>' . t('This form lets administrators configure how fields should be displayed when rendering a user profile page.') . '</p>';
    case 'admin/people/search':
      return '<p>' . t('Enter a simple pattern ("*" may be used as a wildcard match) to search for a username or e-mail address. For example, one may search for "br" and Drupal might return "brian", "brad", and "brenda@example.com".') . '</p>';
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
