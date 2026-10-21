# contact_help()

- **Type:** Function
- **File:** [`modules/contact/contact.module`](_file.md), lines 11–35 · [local source](../../../../source/modules/contact/contact.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module#L11-L35)
- **Module/theme:** contact
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function contact_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function contact_help($path, $arg) {
  switch ($path) {
    case 'admin/help#contact':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Contact module allows visitors to contact site administrators and other users. Users specify a subject, write their message, and can have a copy of their message sent to their own e-mail address. For more information, see the online handbook entry for <a href="@contact">Contact module</a>.', array('@contact' => 'http://drupal.org/documentation/modules/contact/')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('User contact forms') . '</dt>';
      $output .= '<dd>' . t('Site users can be contacted with a user contact form that keeps their e-mail address private. Users may enable or disable their personal contact forms by editing their <em>My account</em> page. If enabled, a <em>Contact</em> tab leads to a personal contact form displayed on their user profile. Site administrators are still able to use the contact form, even if has been disabled. The <em>Contact</em> tab is not shown when you view your own profile.') . '</dd>';
      $output .= '<dt>' . t('Site-wide contact forms') . '</dt>';
      $output .= '<dd>' . t('The <a href="@contact">Contact page</a> provides a simple form for users with the <em>Use the site-wide contact form</em> permission to send comments, feedback, or other requests. You can create categories for directing the contact form messages to a set of defined recipients. Common categories for a business site, for example, might include "Website feedback" (messages are forwarded to website administrators) and "Product information" (messages are forwarded to members of the sales department). E-mail addresses defined within a category are not displayed publicly.', array('@contact' => url('contact'))) . '</p>';
      $output .= '<dt>' . t('Navigation') . '</dt>';
      $output .= '<dd>' . t("When the site-wide contact form is enabled, a link in the main <em>Navigation</em> menu is created, but the link is disabled by default. This menu link can be enabled on the <a href='@menu'>Menus administration page</a>.", array('@contact' => url('contact'), '@menu' => url('admin/structure/menu'))) . '</dd>';
      $output .= '<dt>' . t('Customization') . '</dt>';
      $output .= '<dd>' . t('If you would like additional text to appear on the site-wide or personal contact page, use a block. You can create and edit blocks on the <a href="@blocks">Blocks administration page</a>.', array('@blocks' => url('admin/structure/block'))) . '</dd>';
      $output .= '</dl>';
      return $output;
    case 'admin/structure/contact':
      $output = '<p>' . t('Add one or more categories on this page to set up your site-wide <a href="@form">contact form</a>.', array('@form' => url('contact'))) . '</p>';
      $output .= '<p>' . t('A <em>Contact</em> menu item (disabled by default) is added to the Navigation menu, which you can modify on the <a href="@menu-settings">Menus administration page</a>.', array('@menu-settings' => url('admin/structure/menu'))) . '</p>';
      $output .= '<p>' . t('If you would like additional text to appear on the site-wide contact page, use a block. You can create and edit blocks on the <a href="@blocks">Blocks administration page</a>.', array('@blocks' => url('admin/structure/block'))) . '</p>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/contact/contact.module](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module) · Licensed GPL-2.0-or-later (see LICENSE)._
