# contact_menu()

- **Type:** Function
- **File:** [`modules/contact/contact.module`](_file.md), lines 57–107 · [local source](../../../../source/modules/contact/contact.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module#L57-L107)
- **Module/theme:** contact
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function contact_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function contact_menu() {
  $items['admin/structure/contact'] = array(
    'title' => 'Contact form',
    'description' => 'Create a system contact form and set up categories for the form to use.',
    'page callback' => 'contact_category_list',
    'access arguments' => array('administer contact forms'),
    'file' => 'contact.admin.inc',
  );
  $items['admin/structure/contact/add'] = array(
    'title' => 'Add category',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('contact_category_edit_form'),
    'access arguments' => array('administer contact forms'),
    'type' => MENU_LOCAL_ACTION,
    'weight' => 1,
    'file' => 'contact.admin.inc',
  );
  $items['admin/structure/contact/edit/%contact'] = array(
    'title' => 'Edit contact category',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('contact_category_edit_form', 4),
    'access arguments' => array('administer contact forms'),
    'file' => 'contact.admin.inc',
  );
  $items['admin/structure/contact/delete/%contact'] = array(
    'title' => 'Delete contact',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('contact_category_delete_form', 4),
    'access arguments' => array('administer contact forms'),
    'file' => 'contact.admin.inc',
  );
  $items['contact'] = array(
    'title' => 'Contact',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('contact_site_form'),
    'access arguments' => array('access site-wide contact form'),
    'type' => MENU_SUGGESTED_ITEM,
    'file' => 'contact.pages.inc',
  );
  $items['user/%user/contact'] = array(
    'title' => 'Contact',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('contact_personal_form', 1),
    'type' => MENU_LOCAL_TASK,
    'access callback' => '_contact_personal_tab_access',
    'access arguments' => array(1),
    'weight' => 2,
    'file' => 'contact.pages.inc',
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/contact/contact.module](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module) · Licensed GPL-2.0-or-later (see LICENSE)._
