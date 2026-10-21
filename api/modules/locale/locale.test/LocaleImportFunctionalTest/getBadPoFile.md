# LocaleImportFunctionalTest::getBadPoFile()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1202–1222 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1202-L1222)
- **Class:** [LocaleImportFunctionalTest](../LocaleImportFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function getBadPoFile()
```

## Documentation

```text
Helper function that returns a bad .po file.
```

## Code

```php
  function getBadPoFile() {
    return <<< EOF
msgid ""
msgstr ""
"Project-Id-Version: Drupal 7\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: nplurals=2; plural=(n > 1);\\n"

msgid "Save configuration"
msgstr "Enregistrer la configuration"

msgid "edit"
msgstr "modifier<img SRC="javascript:alert(\'xss\');">"

msgid "delete"
msgstr "supprimer<script>alert('xss');</script>"

EOF;
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
