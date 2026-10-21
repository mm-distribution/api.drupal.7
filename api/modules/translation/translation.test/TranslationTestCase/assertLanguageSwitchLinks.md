# TranslationTestCase::assertLanguageSwitchLinks()

- **Type:** Method
- **File:** [`modules/translation/translation.test`](../_file.md), lines 424–461 · [local source](../../../../../source/modules/translation/translation.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test#L424-L461)
- **Class:** [TranslationTestCase](../TranslationTestCase.md)
- **Module/theme:** translation

## Signature

```php
function assertLanguageSwitchLinks($node, $translation, $find = TRUE, $types = NULL)
```

## Documentation

```text
Tests whether the specified language switch links are found.

@param $node
  The node to display.
@param $translation
  The translation whose link has to be checked.
@param $find
  TRUE if the link must be present in the node page.
@param $types
  The page areas to be checked.

@return
  TRUE if the language switch links are found, FALSE if not.
```

## Code

```php
  function assertLanguageSwitchLinks($node, $translation, $find = TRUE, $types = NULL) {
    if (empty($types)) {
      $types = array('node', 'block-locale');
    }
    elseif (is_string($types)) {
      $types = array($types);
    }

    $result = TRUE;
    $languages = language_list();
    $page_language = $languages[entity_language('node', $node)];
    $translation_language = $languages[$translation->language];
    $url = url("node/$translation->nid", array('language' => $translation_language));

    $this->drupalGet("node/$node->nid", array('language' => $page_language));

    foreach ($types as $type) {
      $args = array('%translation_language' => $translation_language->native, '%page_language' => $page_language->native, '%type' => $type);
      if ($find) {
        $message = format_string('[%page_language] Language switch item found for %translation_language language in the %type page area.', $args);
      }
      else {
        $message = format_string('[%page_language] Language switch item not found for %translation_language language in the %type page area.', $args);
      }

      if (!empty($translation->nid)) {
        $xpath = '//div[contains(@class, :type)]//a[@href=:url]';
      }
      else {
        $xpath = '//div[contains(@class, :type)]//span[contains(@class, "locale-untranslated")]';
      }

      $found = $this->findContentByXPath($xpath, array(':type' => $type, ':url' => $url), $translation_language->native);
      $result = $this->assertTrue($found == $find, $message) && $result;
    }

    return $result;
  }
```

---
_Drupal 7.103 · [modules/translation/translation.test](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test) · Licensed GPL-2.0-or-later (see LICENSE)._
