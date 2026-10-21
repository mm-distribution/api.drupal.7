# image_help()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 44–70 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L44-L70)
- **Module/theme:** image
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function image_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function image_help($path, $arg) {
  switch ($path) {
    case 'admin/help#image':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Image module allows you to manipulate images on your website. It exposes a setting for using the <em>Image toolkit</em>, allows you to configure <em>Image styles</em> that can be used for resizing or adjusting images on display, and provides an <em>Image</em> field for attaching images to content. For more information, see the online handbook entry for <a href="@image">Image module</a>.', array('@image' => 'http://drupal.org/documentation/modules/image')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Manipulating images') . '</dt>';
      $output .= '<dd>' . t('With the Image module you can scale, crop, resize, rotate and desaturate images without affecting the original image using <a href="@image">image styles</a>. When you change an image style, the module automatically refreshes all created images. Every image style must have a name, which will be used in the URL of the generated images. There are two common approaches to naming image styles (which you use will depend on how the image style is being applied):',array('@image' => url('admin/config/media/image-styles')));
      $output .= '<ul><li>' . t('Based on where it will be used: eg. <em>profile-picture</em>') . '</li>';
      $output .= '<li>' . t('Describing its appearance: eg. <em>square-85x85</em>') . '</li></ul>';
      $output .=  t('After you create an image style, you can add effects: crop, scale, resize, rotate, and desaturate (other contributed modules provide additional effects). For example, by combining effects as crop, scale, and desaturate, you can create square, grayscale thumbnails.') . '<dd>';
      $output .= '<dt>' . t('Attaching images to content as fields') . '</dt>';
      $output .= '<dd>' . t("Image module also allows you to attach images to content as fields. To add an image field to a <a href='@content-type'>content type</a>, go to the content type's <em>manage fields</em> page, and add a new field of type <em>Image</em>. Attaching images to content this way allows image styles to be applied and maintained, and also allows you more flexibility when theming.", array('@content-type' => url('admin/structure/types'))) . '</dd>';
      $output .= '</dl>';
      return $output;
    case 'admin/config/media/image-styles':
      return '<p>' . t('Image styles commonly provide thumbnail sizes by scaling and cropping images, but can also add various effects before an image is displayed. When an image is displayed with a style, a new file is created and the original image is left unchanged.') . '</p>';
    case 'admin/config/media/image-styles/edit/%/add/%':
      $effect = image_effect_definition_load($arg[7]);
      return isset($effect['help']) ? ('<p>' . $effect['help'] . '</p>') : NULL;
    case 'admin/config/media/image-styles/edit/%/effects/%':
      $effect = ($arg[5] == 'add') ? image_effect_definition_load($arg[6]) : image_effect_load($arg[7], $arg[5]);
      return isset($effect['help']) ? ('<p>' . $effect['help'] . '</p>') : NULL;
  }
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
