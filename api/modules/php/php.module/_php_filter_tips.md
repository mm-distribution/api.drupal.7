# _php_filter_tips()

- **Type:** Function
- **File:** [`modules/php/php.module`](_file.md), lines 95–131 · [local source](../../../../source/modules/php/php.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/php/php.module#L95-L131)
- **Module/theme:** php

## Signature

```php
function _php_filter_tips($filter, $format, $long = FALSE)
```

## Documentation

```text
Implements callback_filter_tips().

@see php_filter_info()
```

## Code

```php
function _php_filter_tips($filter, $format, $long = FALSE) {
  global $base_url;
  if ($long) {
    $output = '<h4>' . t('Using custom PHP code') . '</h4>';
    $output .= '<p>' . t('Custom PHP code may be embedded in some types of site content, including posts and blocks. While embedding PHP code inside a post or block is a powerful and flexible feature when used by a trusted user with PHP experience, it is a significant and dangerous security risk when used improperly. Even a small mistake when posting PHP code may accidentally compromise your site.') . '</p>';
    $output .= '<p>' . t('If you are unfamiliar with PHP, SQL, or Drupal, avoid using custom PHP code within posts. Experimenting with PHP may corrupt your database, render your site inoperable, or significantly compromise security.') . '</p>';
    $output .= '<p>' . t('Notes:') . '</p>';
    $output .= '<ul><li>' . t('Remember to double-check each line for syntax and logic errors <strong>before</strong> saving.') . '</li>';
    $output .= '<li>' . t('Statements must be correctly terminated with semicolons.') . '</li>';
    $output .= '<li>' . t('Global variables used within your PHP code retain their values after your script executes.') . '</li>';
    $output .= '<li>' . t('<code>register_globals</code> is <strong>turned off</strong>. If you need to use forms, understand and use the functions in <a href="@formapi">the Drupal Form API</a>.', array('@formapi' => url('http://api.drupal.org/api/group/form_api/7'))) . '</li>';
    $output .= '<li>' . t('Use a <code>print</code> or <code>return</code> statement in your code to output content.') . '</li>';
    $output .= '<li>' . t('Develop and test your PHP code using a separate test script and sample database before deploying on a production site.') . '</li>';
    $output .= '<li>' . t('Consider including your custom PHP code within a site-specific module or <code>template.php</code> file rather than embedding it directly into a post or block.') . '</li>';
    $output .= '<li>' . t('Be aware that the ability to embed PHP code within content is provided by the PHP Filter module. If this module is disabled or deleted, then blocks and posts with embedded PHP may display, rather than execute, the PHP code.') . '</li></ul>';
    $output .= '<p>' . t('A basic example: <em>Creating a "Welcome" block that greets visitors with a simple message.</em>') . '</p>';
    $output .= '<ul><li>' . t('<p>Add a custom block to your site, named "Welcome" . With its text format set to "PHP code" (or another format supporting PHP input), add the following in the Block body:</p>
<pre>
print t(\'Welcome visitor! Thank you for visiting.\');
</pre>') . '</li>';
    $output .= '<li>' . t('<p>To display the name of a registered user, use this instead:</p>
<pre>
global $user;
if ($user->uid) {
  print t(\'Welcome @name! Thank you for visiting.\', array(\'@name\' => format_username($user)));
}
else {
  print t(\'Welcome visitor! Thank you for visiting.\');
}
</pre>') . '</li></ul>';
    $output .= '<p>' . t('<a href="@drupal">Drupal.org</a> offers <a href="@php-snippets">some example PHP snippets</a>, or you can create your own with some PHP experience and knowledge of the Drupal system.', array('@drupal' => url('http://drupal.org'), '@php-snippets' => url('http://drupal.org/documentation/customization/php-snippets'))) . '</p>';
    return $output;
  }
  else {
    return t('You may post PHP code. You should include &lt;?php ?&gt; tags.');
  }
}
```

---
_Drupal 7.103 · [modules/php/php.module](https://github.com/drupal/drupal/blob/7.103/modules/php/php.module) · Licensed GPL-2.0-or-later (see LICENSE)._
