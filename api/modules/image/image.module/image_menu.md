# image_menu()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 75–181 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L75-L181)
- **Module/theme:** image
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function image_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function image_menu() {
  $items = array();

  // Generate image derivatives of publicly available files.
  // If clean URLs are disabled, image derivatives will always be served
  // through the menu system.
  // If clean URLs are enabled and the image derivative already exists,
  // PHP will be bypassed.
  $directory_path = file_stream_wrapper_get_instance_by_scheme('public')->getDirectoryPath();
  $items[$directory_path . '/styles/%image_style'] = array(
    'title' => 'Generate image style',
    'page callback' => 'image_style_deliver',
    'page arguments' => array(count(explode('/', $directory_path)) + 1),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  // Generate and deliver image derivatives of private files.
  // These image derivatives are always delivered through the menu system.
  $items['system/files/styles/%image_style'] = array(
    'title' => 'Generate image style',
    'page callback' => 'image_style_deliver',
    'page arguments' => array(3),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['admin/config/media/image-styles'] = array(
    'title' => 'Image styles',
    'description' => 'Configure styles that can be used for resizing or adjusting images on display.',
    'page callback' => 'image_style_list',
    'access arguments' => array('administer image styles'),
    'file' => 'image.admin.inc',
  );
  $items['admin/config/media/image-styles/list'] = array(
    'title' => 'List',
    'description' => 'List the current image styles on the site.',
    'page callback' => 'image_style_list',
    'access arguments' => array('administer image styles'),
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => 1,
    'file' => 'image.admin.inc',
  );
  $items['admin/config/media/image-styles/add'] = array(
    'title' => 'Add style',
    'description' => 'Add a new image style.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('image_style_add_form'),
    'access arguments' => array('administer image styles'),
    'type' => MENU_LOCAL_ACTION,
    'weight' => 2,
    'file' => 'image.admin.inc',
  );
  $items['admin/config/media/image-styles/edit/%image_style'] = array(
    'title' => 'Edit style',
    'description' => 'Configure an image style.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('image_style_form', 5),
    'access arguments' => array('administer image styles'),
    'file' => 'image.admin.inc',
  );
  $items['admin/config/media/image-styles/delete/%image_style'] = array(
    'title' => 'Delete style',
    'description' => 'Delete an image style.',
    'load arguments' => array(NULL, (string) IMAGE_STORAGE_NORMAL),
    'page callback' => 'drupal_get_form',
    'page arguments' => array('image_style_delete_form', 5),
    'access arguments' => array('administer image styles'),
    'file' => 'image.admin.inc',
  );
  $items['admin/config/media/image-styles/revert/%image_style'] = array(
    'title' => 'Revert style',
    'description' => 'Revert an image style.',
    'load arguments' => array(NULL, (string) IMAGE_STORAGE_OVERRIDE),
    'page callback' => 'drupal_get_form',
    'page arguments' => array('image_style_revert_form', 5),
    'access arguments' => array('administer image styles'),
    'file' => 'image.admin.inc',
  );
  $items['admin/config/media/image-styles/edit/%image_style/effects/%image_effect'] = array(
    'title' => 'Edit image effect',
    'description' => 'Edit an existing effect within a style.',
    'load arguments' => array(5, (string) IMAGE_STORAGE_EDITABLE),
    'page callback' => 'drupal_get_form',
    'page arguments' => array('image_effect_form', 5, 7),
    'access arguments' => array('administer image styles'),
    'file' => 'image.admin.inc',
  );
  $items['admin/config/media/image-styles/edit/%image_style/effects/%image_effect/delete'] = array(
    'title' => 'Delete image effect',
    'description' => 'Delete an existing effect from a style.',
    'load arguments' => array(5, (string) IMAGE_STORAGE_EDITABLE),
    'page callback' => 'drupal_get_form',
    'page arguments' => array('image_effect_delete_form', 5, 7),
    'access arguments' => array('administer image styles'),
    'file' => 'image.admin.inc',
  );
  $items['admin/config/media/image-styles/edit/%image_style/add/%image_effect_definition'] = array(
    'title' => 'Add image effect',
    'description' => 'Add a new effect to a style.',
    'load arguments' => array(5),
    'page callback' => 'drupal_get_form',
    'page arguments' => array('image_effect_form', 5, 7),
    'access arguments' => array('administer image styles'),
    'file' => 'image.admin.inc',
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
