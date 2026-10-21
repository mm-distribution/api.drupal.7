# filter_help()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 11–39 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L11-L39)
- **Module/theme:** filter
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function filter_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function filter_help($path, $arg) {
  switch ($path) {
    case 'admin/help#filter':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Filter module allows administrators to configure text formats. A text format defines the HTML tags, codes, and other input allowed in content and comments, and is a key feature in guarding against potentially damaging input from malicious users. For more information, see the online handbook entry for <a href="@filter">Filter module</a>.', array('@filter' => 'http://drupal.org/documentation/modules/filter/')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Configuring text formats') . '</dt>';
      $output .= '<dd>' . t('Configure text formats on the <a href="@formats">Text formats page</a>. <strong>Improper text format configuration is a security risk</strong>. To ensure security, untrusted users should only have access to text formats that restrict them to either plain text or a safe set of HTML tags, since certain HTML tags can allow embedding malicious links or scripts in text. More trusted registered users may be granted permission to use less restrictive text formats in order to create rich content.', array('@formats' => url('admin/config/content/formats'))) . '</dd>';
      $output .= '<dt>' . t('Applying filters to text') . '</dt>';
      $output .= '<dd>' . t('Each text format uses filters to manipulate text, and most formats apply several different filters to text in a specific order. Each filter is designed for a specific purpose, and generally either adds, removes, or transforms elements within user-entered text before it is displayed. A filter does not change the actual content, but instead, modifies it temporarily before it is displayed. One filter may remove unapproved HTML tags, while another automatically adds HTML to make URLs display as clickable links.') . '</dd>';
      $output .= '<dt>' . t('Defining text formats') . '</dt>';
      $output .= '<dd>' . t('One format is included by default: <em>Plain text</em> (which removes all HTML tags). Additional formats may be created by your installation profile when you install Drupal, and more can be created by an administrator on the <a href="@text-formats">Text formats page</a>.', array('@text-formats' => url('admin/config/content/formats'))) . '</dd>';
      $output .= '<dt>' . t('Choosing a text format') . '</dt>';
      $output .= '<dd>' . t('Users with access to more than one text format can use the <em>Text format</em> fieldset to choose between available text formats when creating or editing multi-line content. Administrators can define the text formats available to each user role, and control the order of formats listed in the <em>Text format</em> fieldset on the <a href="@text-formats">Text formats page</a>.', array('@text-formats' => url('admin/config/content/formats'))) . '</dd>';
      $output .= '</dl>';
      return $output;

    case 'admin/config/content/formats':
      $output = '<p>' . t('Text formats define the HTML tags, code, and other formatting that can be used when entering text. <strong>Improper text format configuration is a security risk</strong>. Learn more on the <a href="@filterhelp">Filter module help page</a>.', array('@filterhelp' => url('admin/help/filter'))) . '</p>';
      $output .= '<p>' . t('Text formats are presented on content editing pages in the order defined on this page. The first format available to a user will be selected by default.') . '</p>';
      return $output;

    case 'admin/config/content/formats/%':
      $output = '<p>' . t('A text format contains filters that change the user input, for example stripping out malicious HTML or making URLs clickable. Filters are executed from top to bottom and the order is important, since one filter may prevent another filter from doing its job. For example, when URLs are converted into links before disallowed HTML tags are removed, all links may be removed. When this happens, the order of filters may need to be re-arranged.') . '</p>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
