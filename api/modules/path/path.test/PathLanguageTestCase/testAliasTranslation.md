# PathLanguageTestCase::testAliasTranslation()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 372–477 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L372-L477)
- **Class:** [PathLanguageTestCase](../PathLanguageTestCase.md)
- **Module/theme:** path

## Signature

```php
function testAliasTranslation()
```

## Documentation

```text
Test alias functionality through the admin interfaces.
```

## Code

```php
  function testAliasTranslation() {
    // Set 'page' content type to enable translation.
    variable_set('language_content_type_page', 2);

    $english_node = $this->drupalCreateNode(array('type' => 'page'));
    $english_alias = $this->randomName();

    // Edit the node to set language and path.
    $edit = array();
    $edit['language'] = 'en';
    $edit['path[alias]'] = $english_alias;
    $this->drupalPost('node/' . $english_node->nid . '/edit', $edit, t('Save'));

    // Confirm that the alias works.
    $this->drupalGet($english_alias);
    $this->assertText($english_node->title, 'Alias works.');

    // Translate the node into French.
    $this->drupalGet('node/' . $english_node->nid . '/translate');
    $this->clickLink(t('add translation'));
    $edit = array();
    $langcode = LANGUAGE_NONE;
    $edit["title"] = $this->randomName();
    $edit["body[$langcode][0][value]"] = $this->randomName();
    $french_alias = $this->randomName();
    $edit['path[alias]'] = $french_alias;
    $this->drupalPost(NULL, $edit, t('Save'));

    // Clear the path lookup cache.
    drupal_lookup_path('wipe');

    // Ensure the node was created.
    $french_node = $this->drupalGetNodeByTitle($edit["title"]);
    $this->assertTrue(($french_node), 'Node found in database.');

    // Confirm that the alias works.
    $this->drupalGet('fr/' . $edit['path[alias]']);
    $this->assertText($french_node->title, 'Alias for French translation works.');

    // Confirm that the alias is returned by url().
    drupal_static_reset('language_list');
    drupal_static_reset('locale_url_outbound_alter');
    $languages = language_list();
    $url = url('node/' . $french_node->nid, array('language' => $languages[$french_node->language]));
    $this->assertTrue(strpos($url, $edit['path[alias]']), 'URL contains the path alias.');

    // Confirm that the alias works even when changing language negotiation
    // options. Enable User language detection and selection over URL one.
    $edit = array(
      'language[enabled][locale-user]' => 1,
      'language[weight][locale-user]' => -9,
      'language[enabled][locale-url]' => 1,
      'language[weight][locale-url]' => -8,
    );
    $this->drupalPost('admin/config/regional/language/configure', $edit, t('Save settings'));

    // Change user language preference.
    $edit = array('language' => 'fr');
    $this->drupalPost("user/{$this->web_user->uid}/edit", $edit, t('Save'));

    // Check that the English alias works. In this situation French is the
    // current UI and content language, while URL language is English (since we
    // do not have a path prefix we fall back to the site's default language).
    // We need to ensure that the user language preference is not taken into
    // account while determining the path alias language, because if this
    // happens we have no way to check that the path alias is valid: there is no
    // path alias for French matching the english alias. So drupal_lookup_path()
    // needs to use the URL language to check whether the alias is valid.
    $this->drupalGet($english_alias);
    $this->assertText($english_node->title, 'Alias for English translation works.');

    // Check that the French alias works.
    $this->drupalGet("fr/$french_alias");
    $this->assertText($french_node->title, 'Alias for French translation works.');

    // Disable URL language negotiation.
    $edit = array('language[enabled][locale-url]' => FALSE);
    $this->drupalPost('admin/config/regional/language/configure', $edit, t('Save settings'));

    // Check that the English alias still works.
    $this->drupalGet($english_alias);
    $this->assertText($english_node->title, 'Alias for English translation works.');

    // Check that the French alias is not available. We check the unprefixed
    // alias because we disabled URL language negotiation above. In this
    // situation only aliases in the default language and language neutral ones
    // should keep working.
    $this->drupalGet($french_alias);
    $this->assertResponse(404, 'Alias for French translation is unavailable when URL language negotiation is disabled.');

    // drupal_lookup_path() has an internal static cache. Check to see that
    // it has the appropriate contents at this point.
    drupal_lookup_path('wipe');
    $french_node_path = drupal_lookup_path('source', $french_alias, $french_node->language);
    $this->assertEqual($french_node_path, 'node/' . $french_node->nid, 'Normal path works.');
    // Second call should return the same path.
    $french_node_path = drupal_lookup_path('source', $french_alias, $french_node->language);
    $this->assertEqual($french_node_path, 'node/' . $french_node->nid, 'Normal path is the same.');

    // Confirm that the alias works.
    $french_node_alias = drupal_lookup_path('alias', 'node/' . $french_node->nid, $french_node->language);
    $this->assertEqual($french_node_alias, $french_alias, 'Alias works.');
    // Second call should return the same alias.
    $french_node_alias = drupal_lookup_path('alias', 'node/' . $french_node->nid, $french_node->language);
    $this->assertEqual($french_node_alias, $french_alias, 'Alias is the same.');
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
