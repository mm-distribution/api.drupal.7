# file_help()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 14–31 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L14-L31)
- **Module/theme:** file
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function file_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function file_help($path, $arg) {
  switch ($path) {
    case 'admin/help#file':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The File module defines a <em>File</em> field type for the Field module, which lets you manage and validate uploaded files attached to content on your site (see the <a href="@field-help">Field module help page</a> for more information about fields). For more information, see the online handbook entry for <a href="@file">File module</a>.', array('@field-help' => url('admin/help/field'), '@file' => 'http://drupal.org/documentation/modules/file')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Attaching files to content') . '</dt>';
      $output .= '<dd>' . t('The File module allows users to attach files to content (e.g., PDF files, spreadsheets, etc.), when a <em>File</em> field is added to a given content type using the <a href="@fieldui-help">Field UI module</a>. You can add validation options to your File field, such as specifying a maximum file size and allowed file extensions.', array('@fieldui-help' => url('admin/help/field_ui'))) . '</dd>';
      $output .= '<dt>' . t('Managing attachment display') . '</dt>';
      $output .= '<dd>' . t('When you attach a file to content, you can specify whether it is <em>listed</em> or not. Listed files are displayed automatically in a section at the bottom of your content; non-listed files are available for embedding in your content, but are not included in the list at the bottom.') . '</dd>';
      $output .= '<dt>' . t('Managing file locations') . '</dt>';
      $output .= '<dd>' . t("When you create a File field, you can specify a directory where the files will be stored, which can be within either the <em>public</em> or <em>private</em> files directory. Files in the public directory can be accessed directly through the web server; when public files are listed, direct links to the files are used, and anyone who knows a file's URL can download the file. Files in the private directory are not accessible directly through the web server; when private files are listed, the links are Drupal path requests. This adds to server load and download time, since Drupal must start up and resolve the path for each file download request, but allows for access restrictions.") . '</dd>';
      $output .= '</dl>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
