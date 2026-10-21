# TranslationTestCase::createPage()

- **Type:** Method
- **File:** [`modules/translation/translation.test`](../_file.md), lines 330–346 · [local source](../../../../../source/modules/translation/translation.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test#L330-L346)
- **Class:** [TranslationTestCase](../TranslationTestCase.md)
- **Module/theme:** translation

## Signature

```php
function createPage($title, $body, $language = NULL)
```

## Documentation

```text
Creates a "Basic page" in the specified language.

@param $title
  The title of a basic page in the specified language.
@param $body
  The body of a basic page in the specified language.
@param $language
  (optional) Language code.

@return
  A node object.
```

## Code

```php
  function createPage($title, $body, $language = NULL) {
    $edit = array();
    $langcode = LANGUAGE_NONE;
    $edit["title"] = $title;
    $edit["body[$langcode][0][value]"] = $body;
    if (!empty($language)) {
      $edit['language'] = $language;
    }
    $this->drupalPost('node/add/page', $edit, t('Save'));
    $this->assertRaw(t('Basic page %title has been created.', array('%title' => $title)), 'Basic page created.');

    // Check to make sure the node was created.
    $node = $this->drupalGetNodeByTitle($title);
    $this->assertTrue($node, 'Node found in database.');

    return $node;
  }
```

---
_Drupal 7.103 · [modules/translation/translation.test](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test) · Licensed GPL-2.0-or-later (see LICENSE)._
