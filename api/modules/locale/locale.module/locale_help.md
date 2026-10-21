# locale_help()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 20–68 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L20-L68)
- **Module/theme:** locale
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function locale_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function locale_help($path, $arg) {
  switch ($path) {
    case 'admin/help#locale':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Locale module allows your Drupal site to be presented in languages other than the default English, and to be multilingual. The Locale module works by maintaining a database of translations, and examining text as it is about to be displayed. When a translation of the text is available in the language to be displayed, the translation is displayed rather than the original text. When a translation is unavailable, the original text is displayed, and then stored for review by a translator. For more information, see the online handbook entry for <a href="@locale">Locale module</a>.', array('@locale' => 'http://drupal.org/documentation/modules/locale/')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Translating interface text') . '</dt>';
      $output .= '<dd>' . t('Translations of text in the Drupal interface may be provided by:');
      $output .= '<ul>';
      $output .= '<li>' . t("Translating within your site, using the Locale module's integrated <a href='@translate'>translation interface</a>.", array('@translate' => url('admin/config/regional/translate'))) . '</li>';
      $output .= '<li>' . t('Importing files from a set of existing translations, known as a translation package. A translation package enables the display of a specific version of Drupal in a specific language, and contains files in the Gettext Portable Object (<em>.po</em>) format. Although not all languages are available for every version of Drupal, translation packages for many languages are available for download from the <a href="@translations">Drupal translations page</a>.', array('@translations' => 'http://localize.drupal.org')) . '</li>';
      $output .= '<li>' . t("If an existing translation package does not meet your needs, the Gettext Portable Object (<em>.po</em>) files within a package may be modified, or new <em>.po</em> files may be created, using a desktop Gettext editor. The Locale module's <a href='@import'>import</a> feature allows the translated strings from a new or modified <em>.po</em> file to be added to your site. The Locale module's <a href='@export'>export</a> feature generates files from your site's translated strings, that can either be shared with others or edited offline by a Gettext translation editor.", array('@import' => url('admin/config/regional/translate/import'), '@export' => url('admin/config/regional/translate/export'))) . '</li>';
      $output .= '</ul></dd>';
      $output .= '<dt>' . t('Configuring a multilingual site') . '</dt>';
      $output .= '<dd>' . t("Language negotiation allows your site to automatically change language based on the domain or path used for each request. Users may (optionally) select their preferred language on their <em>My account</em> page, and your site can be configured to honor a web browser's preferred language settings. Site content can be translated using the <a href='@content-help'>Content translation module</a>.", array('@content-help' => url('admin/help/translation'))) . '</dd>';
      $output .= '</dl>';
      return $output;
    case 'admin/config/regional/language':
      $output = '<p>' . t('With multiple languages enabled, interface text can be translated, registered users may select their preferred language, and authors can assign a specific language to content. <a href="@translations">Download contributed translations</a> from Drupal.org.', array('@translations' => 'http://localize.drupal.org')) . '</p>';
      return $output;
    case 'admin/config/regional/language/add':
      return '<p>' . t('Add a language to be supported by your site. If your desired language is not available in the <em>Language name</em> drop-down, click <em>Custom language</em> and provide a language code and other details manually. When providing a language code manually, be sure to enter a standardized language code, since this code may be used by browsers to determine an appropriate display language.') . '</p>';
    case 'admin/config/regional/language/configure':
      $output = '<p>' . t("Define how to decide which language is used to display page elements (primarily text provided by Drupal and modules, such as field labels and help text). This decision is made by evaluating a series of detection methods for languages; the first detection method that gets a result will determine which language is used for that type of text. Define the order of evaluation of language detection methods on this page.") . '</p>';
      return $output;
    case 'admin/config/regional/language/configure/session':
      $output = '<p>' . t('Determine the language from a request/session parameter. Example: "http://example.com?language=de" sets language to German based on the use of "de" within the "language" parameter.') . '</p>';
      return $output;
    case 'admin/config/regional/translate':
      $output = '<p>' . t('This page provides an overview of available translatable strings. Drupal displays translatable strings in text groups; modules may define additional text groups containing other translatable strings. Because text groups provide a method of grouping related strings, they are often used to focus translation efforts on specific areas of the Drupal interface.') . '</p>';
      $output .= '<p>' . t('See the <a href="@languages">Languages page</a> for more information on adding support for additional languages.', array('@languages' => url('admin/config/regional/language'))) . '</p>';
      return $output;
    case 'admin/config/regional/translate/import':
      $output = '<p>' . t('This page imports the translated strings contained in an individual Gettext Portable Object (<em>.po</em>) file. Normally distributed as part of a translation package (each translation package may contain several <em>.po</em> files), a <em>.po</em> file may need to be imported after offline editing in a Gettext translation editor. Importing an individual <em>.po</em> file may be a lengthy process.') . '</p>';
      $output .= '<p>' . t('Note that the <em>.po</em> files within a translation package are imported automatically (if available) when new modules or themes are enabled, or as new languages are added. Since this page only allows the import of one <em>.po</em> file at a time, it may be simpler to download and extract a translation package into your Drupal installation directory and <a href="@language-add">add the language</a> (which automatically imports all <em>.po</em> files within the package). Translation packages are available for download on the <a href="@translations">Drupal translation page</a>.', array('@language-add' => url('admin/config/regional/language/add'), '@translations' => 'http://localize.drupal.org')) . '</p>';
      return $output;
    case 'admin/config/regional/translate/export':
      return '<p>' . t('This page exports the translated strings used by your site. An export file may be in Gettext Portable Object (<em>.po</em>) form, which includes both the original string and the translation (used to share translations with others), or in Gettext Portable Object Template (<em>.pot</em>) form, which includes the original strings only (used to create new translations with a Gettext translation editor).') . '</p>';
    case 'admin/config/regional/translate/translate':
      return '<p>' . t('This page allows a translator to search for specific translated and untranslated strings, and is used when creating or editing translations. (Note: For translation tasks involving many strings, it may be more convenient to <a href="@export">export</a> strings for offline editing in a desktop Gettext translation editor.) Searches may be limited to strings found within a specific text group or in a specific language.', array('@export' => url('admin/config/regional/translate/export'))) . '</p>';
    case 'admin/structure/block/manage/%/%':
      if ($arg[4] == 'locale' && $arg[5] == 'language') {
        return '<p>' . t('This block is only shown if <a href="@languages">at least two languages are enabled</a> and <a href="@configuration">language negotiation</a> is set to <em>URL</em> or <em>Session</em>.', array('@languages' => url('admin/config/regional/language'), '@configuration' => url('admin/config/regional/language/configure'))) . '</p>';
      }
      break;
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
