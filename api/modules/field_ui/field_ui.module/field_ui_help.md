# field_ui_help()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.module`](_file.md), lines 10–47 · [local source](../../../../source/modules/field_ui/field_ui.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module#L10-L47)
- **Module/theme:** field_ui
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function field_ui_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function field_ui_help($path, $arg) {
  switch ($path) {
    case 'admin/help#field_ui':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Field UI module provides an administrative user interface (UI) for attaching and managing fields. Fields can be defined at the content-type level for content items and comments, at the vocabulary level for taxonomy terms, and at the site level for user accounts. Other modules may also enable fields to be defined for their data. Field types (text, image, number, etc.) are defined by modules, and collected and managed by the <a href="@field">Field module</a>. For more information, see the online handbook entry for <a href="@field_ui" target="_blank">Field UI module</a>.', array('@field' => url('admin/help/field'), '@field_ui' => 'http://drupal.org/documentation/modules/field-ui')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Planning fields') . '</dt>';
      $output .= '<dd>' . t('There are several decisions you will need to make before defining a field for content, comments, etc.:') . '<dl>';
      $output .= '<dt>' . t('What the field will be called') . '</dt>';
      $output .= '<dd>' . t('A field has a <em>label</em> (the name displayed in the user interface) and a <em>machine name</em> (the name used internally). The label can be changed after you create the field, if needed, but the machine name cannot be changed after you have created the field.') . '</li>';
      $output .= '<dt>' . t('What type of data the field will store') . '</dt>';
      $output .= '<dd>' . t('Each field can store one type of data (text, number, file, etc.). When you define a field, you choose a particular <em>field type</em>, which corresponds to the type of data you want to store. The field type cannot be changed after you have created the field.') . '</dd>';
      $output .= '<dt>' . t('How the data will be input and displayed') . '</dt>';
      $output .= '<dd>' . t('Each field type has one or more available <em>widgets</em> associated with it; each widget provides a mechanism for data input when you are editing (text box, select list, file upload, etc.). Each field type also has one or more display options, which determine how the field is displayed to site visitors. The widget and display options can be changed after you have created the field.') . '</dd>';
      $output .= '<dt>' . t('How many values the field will store') . '</dt>';
      $output .= '<dd>' . t('You can store one value, a specific maximum number of values, or an unlimited number of values in each field. For example, an employee identification number field might store a single number, whereas a phone number field might store multiple phone numbers. This setting can be changed after you have created the field, but if you reduce the maximum number of values, you may lose information.') . '</dd>';
      $output .= '</dl>';
      $output .= '<dt>' . t('Reusing fields') . '</dt>';
      $output .= '<dd>' . t('Once you have defined a field, you can reuse it. For example, if you define a custom image field for one content type, and you need to have an image field with the same parameters on another content type, you can add the same field to the second content type, in the <em>Add existing field</em> area of the user interface. You could also add this field to a taxonomy vocabulary, comments, user accounts, etc.') . '</dd>';
      $output .= '<dd>' . t('Some settings of a reused field are unique to each use of the field; others are shared across all places you use the field. For example, the label of a text field is unique to each use, while the setting for the number of values is shared.') . '</dd>';
      $output .= '<dd>' . t('There are two main reasons for reusing fields. First, reusing fields can save you time over defining new fields. Second, reusing fields also allows you to display, filter, group, and sort content together by field across content types. For example, the contributed Views module allows you to create lists and tables of content. So if you use the same field on multiple content types, you can create a View containing all of those content types together displaying that field, sorted by that field, and/or filtered by that field.') . '</dd>';
      $output .= '<dt>' . t('Fields on content items') . '</dt>';
      $output .= '<dd>' . t('Fields on content items are defined at the content-type level, on the <em>Manage fields</em> tab of the content type edit page (which you can reach from the <a href="@types">Content types page</a>). When you define a field for a content type, each content item of that type will have that field added to it. Some fields, such as the Title and Body, are provided for you when you create a content type, or are provided on content types created by your installation profile.', array('@types' => url('admin/structure/types'))) . '</dd>';
      $output .= '<dt>' . t('Fields on taxonomy terms') . '</dt>';
      $output .= '<dd>' . t('Fields on taxonomy terms are defined at the taxonomy vocabulary level, on the <em>Manage fields</em> tab of the vocabulary edit page (which you can reach from the <a href="@taxonomy">Taxonomy page</a>). When you define a field for a vocabulary, each term in that vocabulary will have that field added to it. For example, you could define an image field for a vocabulary to store an icon with each term.', array('@taxonomy' => url('admin/structure/taxonomy'))) . '</dd>';
      $output .= '<dt>' . t('Fields on user accounts') . '</dt>';
      $output .= '<dd>' . t('Fields on user accounts are defined on a site-wide basis on the <a href="@fields">Manage fields tab</a> of the <a href="@accounts">Account settings</a> page. When you define a field for user accounts, each user account will have that field added to it. For example, you could add a long text field to allow users to include a biography.', array('@fields' => url('admin/config/people/accounts/fields'), '@accounts' => url('admin/config/people/accounts'))) . '</dd>';
      $output .= '<dt>' . t('Fields on comments') . '</dt>';
      $output .= '<dd>' . t('Fields on comments are defined at the content-type level, on the <em>Comment fields</em> tab of the content type edit page (which you can reach from the <a href="@types">Content types page</a>). When you add a field for comments, each comment on a content item of that type will have that field added to it. For example, you could add a website field to the comments on forum posts, to allow forum commenters to add a link to their website.', array('@types' => url('admin/structure/types'))) . '</dd>';
      $output .= '</dl>';
      return $output;

    case 'admin/reports/fields':
      return '<p>' . t('This list shows all fields currently in use for easy reference.') . '</p>';
  }
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.module](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module) · Licensed GPL-2.0-or-later (see LICENSE)._
