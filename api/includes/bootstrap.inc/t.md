# t()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1803–1836 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1803-L1836)
- **Topics:** [sanitization](../../topics/sanitization.md)

## Signature

```php
function t($string, array $args = array(), array $options = array())
```

## Documentation

```text
Translates a string to the current language or to a given language.

The t() function serves two purposes. First, at run-time it translates
user-visible text into the appropriate language. Second, various mechanisms
that figure out what text needs to be translated work off t() -- the text
inside t() calls is added to the database of strings to be translated.
These strings are expected to be in English, so the first argument should
always be in English. To enable a fully-translatable site, it is important
that all human-readable text that will be displayed on the site or sent to
a user is passed through the t() function, or a related function. See the
@link http://drupal.org/node/322729 Localization API @endlink pages for
more information, including recommendations on how to break up or not
break up strings for translation.

@section sec_translating_vars Translating Variables
You should never use t() to translate variables, such as calling
@code t($text); @endcode, unless the text that the variable holds has been
passed through t() elsewhere (e.g., $text is one of several translated
literal strings in an array). It is especially important never to call
@code t($user_text); @endcode, where $user_text is some text that a user
entered - doing that can lead to cross-site scripting and other security
problems. However, you can use variable substitution in your string, to put
variable text such as user names or link URLs into translated text. Variable
substitution looks like this:
@code
$text = t("@name's blog", array('@name' => format_username($account)));
@endcode
Basically, you can put variables like @name into your string, and t() will
substitute their sanitized values at translation time. (See the
Localization API pages referenced above and the documentation of
format_string() for details about how to define variables in your string.)
Translators can then rearrange the string as necessary for the language
(e.g., in Spanish, it might be "blog de @name").

@section sec_alt_funcs_install Use During Installation Phase
During the Drupal installation phase, some resources used by t() wil not be
available to code that needs localization. See st() and get_t() for
alternatives.

@section sec_context String context
Matching source strings are normally only translated once, and the same
translation is used everywhere that has a matching string. However, in some
cases, a certain English source string needs to have multiple translations.
One example of this is the string "May", which could be used as either a
full month name or a 3-letter abbreviated month. In other languages where
the month name for May has more than 3 letters, you would need to provide
two different translations (one for the full name and one abbreviated), and
the correct form would need to be chosen, depending on how "May" is being
used. To facilitate this, the "May" string should be provided with two
different contexts in the $options parameter when calling t(). For example:
@code
t('May', array(), array('context' => 'Long month name')
t('May', array(), array('context' => 'Abbreviated month name')
@endcode
See https://localize.drupal.org/node/2109 for more information.

@param $string
  A string containing the English string to translate.
@param $args
  An associative array of replacements to make after translation. Based
  on the first character of the key, the value is escaped and/or themed.
  See format_string() for details.
@param $options
  An associative array of additional options, with the following elements:
  - 'langcode' (defaults to the current language): The language code to
    translate to a language other than what is used to display the page.
  - 'context' (defaults to the empty context): A string giving the context
    that the source string belongs to. See @ref sec_context above for more
    information.

@return
  The translated string.

@see st()
@see get_t()
@see format_string()
@ingroup sanitization
```

## Code

```php
function t($string, array $args = array(), array $options = array()) {
  global $language;
  static $custom_strings;

  // Merge in default.
  if (empty($options['langcode'])) {
    $options['langcode'] = isset($language->language) ? $language->language : 'en';
  }
  if (empty($options['context'])) {
    $options['context'] = '';
  }

  // First, check for an array of customized strings. If present, use the array
  // *instead of* database lookups. This is a high performance way to provide a
  // handful of string replacements. See settings.php for examples.
  // Cache the $custom_strings variable to improve performance.
  if (!isset($custom_strings[$options['langcode']])) {
    $custom_strings[$options['langcode']] = variable_get('locale_custom_strings_' . $options['langcode'], array());
  }
  // Custom strings work for English too, even if locale module is disabled.
  if (isset($custom_strings[$options['langcode']][$options['context']][$string])) {
    $string = $custom_strings[$options['langcode']][$options['context']][$string];
  }
  // Translate with locale module if enabled.
  elseif ($options['langcode'] != 'en' && function_exists('locale')) {
    $string = locale($string, $options['context'], $options['langcode']);
  }
  if (empty($args)) {
    return $string;
  }
  else {
    return format_string($string, $args);
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
