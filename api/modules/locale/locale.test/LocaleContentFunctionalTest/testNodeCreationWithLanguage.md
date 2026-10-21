# LocaleContentFunctionalTest::testNodeCreationWithLanguage()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2297–2322 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2297-L2322)
- **Class:** [LocaleContentFunctionalTest](../LocaleContentFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testNodeCreationWithLanguage()
```

## Documentation

```text
Verifies that nodes may be created with different languages.
```

## Code

```php
  function testNodeCreationWithLanguage() {
    // Create an admin user and log them in.
    $perms = array(
      // Standard node permissions.
      'create page content',
      'administer content types',
      'administer nodes',
      'bypass node access',
      // Locale.
      'administer languages',
    );
    $web_user = $this->drupalCreateUser($perms);
    $this->drupalLogin($web_user);

    // Create some test nodes using different langcodes.
    foreach (array(LANGUAGE_NONE, 'en', 'fr') as $langcode) {
      $node_args = array(
        'type' => 'page',
        'promote' => 1,
        'language' => $langcode,
      );
      $node = $this->drupalCreateNode($node_args);
      $node_reloaded = node_load($node->nid, NULL, TRUE);
      $this->assertEqual($node_reloaded->language, $langcode, format_string('The language code of the node was successfully set to @langcode.', array('@langcode' => $langcode)));
    }
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
