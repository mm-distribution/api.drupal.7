# TranslationTestCase::createTranslation()

- **Type:** Method
- **File:** [`modules/translation/translation.test`](../_file.md), lines 363–383 · [local source](../../../../../source/modules/translation/translation.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test#L363-L383)
- **Class:** [TranslationTestCase](../TranslationTestCase.md)
- **Module/theme:** translation

## Signature

```php
function createTranslation($node, $title, $body, $language)
```

## Documentation

```text
Creates a translation for a basic page in the specified language.

@param $node
  The basic page to create the translation for.
@param $title
  The title of a basic page in the specified language.
@param $body
  The body of a basic page in the specified language.
@param $language
  Language code.

@return
  Translation object.
```

## Code

```php
  function createTranslation($node, $title, $body, $language) {
    $this->drupalGet('node/add/page', array('query' => array('translation' => $node->nid, 'target' => $language)));

    $langcode = LANGUAGE_NONE;
    $body_key = "body[$langcode][0][value]";
    $this->assertFieldByXPath('//input[@id="edit-title"]', $node->title, "Original title value correctly populated.");
    $this->assertFieldByXPath("//textarea[@name='$body_key']", $node->body[LANGUAGE_NONE][0]['value'], "Original body value correctly populated.");

    $edit = array();
    $edit["title"] = $title;
    $edit[$body_key] = $body;
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertRaw(t('Basic page %title has been created.', array('%title' => $title)), 'Translation created.');

    // Check to make sure that translation was successful.
    $translation = $this->drupalGetNodeByTitle($title);
    $this->assertTrue($translation, 'Node found in database.');
    $this->assertTrue($translation->tnid == $node->nid, 'Translation set id correctly stored.');

    return $translation;
  }
```

---
_Drupal 7.103 · [modules/translation/translation.test](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test) · Licensed GPL-2.0-or-later (see LICENSE)._
