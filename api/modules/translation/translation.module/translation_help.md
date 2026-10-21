# translation_help()

- **Type:** Function
- **File:** [`modules/translation/translation.module`](_file.md), lines 30–52 · [local source](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module#L30-L52)
- **Module/theme:** translation
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function translation_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function translation_help($path, $arg) {
  switch ($path) {
    case 'admin/help#translation':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Content translation module allows content to be translated into different languages. Working with the <a href="@locale">Locale module</a> (which manages enabled languages and provides translation for the site interface), the Content translation module is key to creating and maintaining translated site content. For more information, see the online handbook entry for <a href="@translation">Content translation module</a>.', array('@locale' => url('admin/help/locale'), '@translation' => 'http://drupal.org/documentation/modules/translation/')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Configuring content types for translation') . '</dt>';
      $output .= '<dd>' . t('To configure a particular content type for translation, visit the <a href="@content-types">Content types</a> page, and click the <em>edit</em> link for the content type. In the <em>Publishing options</em> section, select <em>Enabled, with translation</em> under <em>Multilingual support</em>.', array('@content-types' => url('admin/structure/types'))) . '</dd>';
      $output .= '<dt>' . t('Assigning a language to content') . '</dt>';
      $output .= '<dd>' . t('Use the <em>Language</em> drop down to select the appropriate language when creating or editing content.') . '</dd>';
      $output .= '<dt>' . t('Translating content') . '</dt>';
      $output .= '<dd>' . t('Users with the <em>translate content</em> permission can translate content, if the content type has been configured to allow translations. To translate content, select the <em>Translation</em> tab when viewing the content, select the language for which you wish to provide content, and then enter the content.') . '</dd>';
      $output .= '<dt>' . t('Maintaining translations') . '</dt>';
      $output .= '<dd>' . t('If editing content in one language requires that translated versions also be updated to reflect the change, use the <em>Flag translations as outdated</em> check box to mark the translations as outdated and in need of revision. Individual translations may also be marked for revision by selecting the <em>This translation needs to be updated</em> check box on the translation editing form.') . '</dd>';
      $output .= '</dl>';
      return $output;
    case 'node/%/translate':
      $output = '<p>' . t('Translations of a piece of content are managed with translation sets. Each translation set has one source post and any number of translations in any of the <a href="!languages">enabled languages</a>. All translations are tracked to be up to date or outdated based on whether the source post was modified significantly.', array('!languages' => url('admin/config/regional/language'))) . '</p>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/translation/translation.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · Licensed GPL-2.0-or-later (see LICENSE)._
