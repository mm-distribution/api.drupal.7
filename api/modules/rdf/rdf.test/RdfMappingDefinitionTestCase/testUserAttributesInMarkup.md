# RdfMappingDefinitionTestCase::testUserAttributesInMarkup()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 355–396 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L355-L396)
- **Class:** [RdfMappingDefinitionTestCase](../RdfMappingDefinitionTestCase.md)
- **Module/theme:** rdf

## Signature

```php
function testUserAttributesInMarkup()
```

## Documentation

```text
Create a random user and ensure the default mapping for user is used.
```

## Code

```php
  function testUserAttributesInMarkup() {
    // Create two users, one with access to user profiles.
    $user1 = $this->drupalCreateUser(array('access user profiles'));
    $user2 = $this->drupalCreateUser();
    $username = $user2->name;
    $this->drupalLogin($user1);
    // Browse to the user profile page.
    $this->drupalGet('user/' . $user2->uid);
    // Ensure the default bundle mapping for user is used on the user profile
    // page. These attributes come from the user default bundle definition.
    $account_uri = url('user/' . $user2->uid);
    $person_uri = url('user/' . $user2->uid, array('fragment' => 'me'));

    $user2_profile_about = $this->xpath('//div[@class="profile" and @typeof="sioc:UserAccount" and @about=:account-uri]', array(
      ':account-uri' => $account_uri,
    ));
    $this->assertTrue(!empty($user2_profile_about), 'RDFa markup found on user profile page');

    $user_account_holder = $this->xpath('//meta[contains(@typeof, "foaf:Person") and @about=:person-uri and @resource=:account-uri and contains(@rel, "foaf:account")]', array(
      ':person-uri' => $person_uri,
      ':account-uri' => $account_uri,
    ));
    $this->assertTrue(!empty($user_account_holder), 'URI created for account holder and username set on sioc:UserAccount.');

    $user_username = $this->xpath('//meta[@about=:account-uri and contains(@property, "foaf:name") and @content=:username]', array(
      ':account-uri' => $account_uri,
      ':username' => $username,
    ));
    $this->assertTrue(!empty($user_username), 'foaf:name set on username.');

    // User 2 creates node.
    $this->drupalLogin($user2);
    $node = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1));
    $this->drupalLogin($user1);
    $this->drupalGet('node/' . $node->nid);
    // Ensures the default bundle mapping for user is used on the Authored By
    // information on the node.
    $author_about = $this->xpath('//a[@typeof="sioc:UserAccount" and @about=:account-uri and @property="foaf:name" and @datatype="" and contains(@xml:lang, "")]', array(
      ':account-uri' => $account_uri,
    ));
    $this->assertTrue(!empty($author_about), 'RDFa markup found on author information on post. xml:lang on username is set to empty string.');
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
