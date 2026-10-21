# DrupalWebTestCase

- **Type:** Class
- **File:** [`modules/simpletest/drupal_web_test_case.php`](_file.md), lines 849–4048 · [local source](../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L849-L4048)
- **Module/theme:** simpletest

## Signature

```php
class DrupalWebTestCase extends DrupalTestCase
```

## Documentation

```text
Test case for typical Drupal tests.
```

## Properties

### $profile

```php
protected $profile = 'standard';
```

```text
The profile to install as a basis for testing.

@var string
```

### $url

```php
protected $url;
```

```text
The URL currently loaded in the internal browser.

@var string
```

### $curlHandle

```php
protected $curlHandle;
```

```text
The handle of the current cURL connection.

@var resource
```

### $headers

```php
protected $headers;
```

```text
The headers of the page currently loaded in the internal browser.

@var Array
```

### $content

```php
protected $content;
```

```text
The content of the page currently loaded in the internal browser.

@var string
```

### $plainTextContent

```php
protected $plainTextContent;
```

```text
The content of the page currently loaded in the internal browser (plain text version).

@var string
```

### $drupalSettings

```php
protected $drupalSettings;
```

```text
The value of the Drupal.settings JavaScript variable for the page currently loaded in the internal browser.

@var Array
```

### $elements

```php
protected $elements = NULL;
```

```text
The parsed version of the page.

@var SimpleXMLElement
```

### $loggedInUser

```php
protected $loggedInUser = FALSE;
```

```text
The current user logged in using the internal browser.

@var bool
```

### $cookieFile

```php
protected $cookieFile = NULL;
```

```text
The current cookie file used by cURL.

We do not reuse the cookies in further runs, so we do not need a file
but we still need cookie handling, so we set the jar to NULL.
```

### $cookies

```php
protected $cookies = array();
```

```text
The cookies of the page currently loaded in the internal browser.

@var array
```

### $additionalCurlOptions

```php
protected $additionalCurlOptions = array();
```

```text
Additional cURL options.

DrupalWebTestCase itself never sets this but always obeys what is set.
```

### $originalUser

```php
protected $originalUser = NULL;
```

```text
The original user, before it was changed to a clean uid = 1 for testing purposes.

@var object
```

### $originalShutdownCallbacks

```php
protected $originalShutdownCallbacks = array();
```

```text
The original shutdown handlers array, before it was cleaned for testing purposes.

@var array
```

### $httpauth_method

```php
protected $httpauth_method = CURLAUTH_BASIC;
```

```text
HTTP authentication method
```

### $httpauth_credentials

```php
protected $httpauth_credentials = NULL;
```

```text
HTTP authentication credentials (<username>:<password>).
```

### $session_name

```php
protected $session_name = NULL;
```

```text
The current session name, if available.
```

### $session_id

```php
protected $session_id = NULL;
```

```text
The current session ID, if available.
```

### $generatedTestFiles

```php
protected $generatedTestFiles = FALSE;
```

```text
Whether the files were copied to the test files directory.
```

### $redirect_count

```php
protected $redirect_count;
```

```text
The number of redirects followed during the handling of a request.
```

### $originalLanguageUrl

```php
protected $originalLanguageUrl;
```

```text
The original language URL.
```

### $originalProfile

```php
protected $originalProfile;
```

```text
The original active installation profile.
```

### $originalCleanUrl

```php
protected $originalCleanUrl;
```

```text
The original clean_url variable value.
```

### $public_files_directory

```php
protected $public_files_directory;
```

```text
The public files directory created for testing purposes.
```

### $private_files_directory

```php
protected $private_files_directory;
```

```text
The private files directory created for testing purposes.
```

### $temp_files_directory

```php
protected $temp_files_directory;
```

```text
The temporary files directory created for testing purposes.
```

## Methods (derived index)

- [__construct()](DrupalWebTestCase/__construct.md) — Constructor for DrupalWebTestCase.
- [drupalGetNodeByTitle()](DrupalWebTestCase/drupalGetNodeByTitle.md) — Get a node from the database based on its title.
- [drupalCreateNode()](DrupalWebTestCase/drupalCreateNode.md) — Creates a node based on default settings.
- [drupalCreateContentType()](DrupalWebTestCase/drupalCreateContentType.md) — Creates a custom content type based on default settings.
- [drupalGetTestFiles()](DrupalWebTestCase/drupalGetTestFiles.md) — Get a list files that can be used in tests.
- [drupalCompareFiles()](DrupalWebTestCase/drupalCompareFiles.md) — Compare two files based on size and file name.
- [drupalCreateUser()](DrupalWebTestCase/drupalCreateUser.md) — Create a user with a given set of permissions.
- [drupalCreateRole()](DrupalWebTestCase/drupalCreateRole.md) — Creates a role with specified permissions.
- [checkPermissions()](DrupalWebTestCase/checkPermissions.md) — Check to make sure that the array of permissions are valid.
- [drupalLogin()](DrupalWebTestCase/drupalLogin.md) — Log in a user with the internal browser.
- [drupalGetToken()](DrupalWebTestCase/drupalGetToken.md) — Generate a token for the currently logged in user.
- [drupalLogout()](DrupalWebTestCase/drupalLogout.md)
- [prepareDatabasePrefix()](DrupalWebTestCase/prepareDatabasePrefix.md) — Generates a database prefix for running tests.
- [changeDatabasePrefix()](DrupalWebTestCase/changeDatabasePrefix.md) — Changes the database connection to the prefixed one.
- [prepareEnvironment()](DrupalWebTestCase/prepareEnvironment.md) — Prepares the current environment for running the test.
- [loadSetupCache()](DrupalWebTestCase/loadSetupCache.md) — Copies the cached tables and files for a cached installation setup.
- [getSetupCacheKey()](DrupalWebTestCase/getSetupCacheKey.md) — Returns the cache key used for the setup caching.
- [storeSetupCache()](DrupalWebTestCase/storeSetupCache.md) — Store the installation setup to a cache.
- [copySetupCache()](DrupalWebTestCase/copySetupCache.md) — Copy the setup cache from/to another table and files directory.
- [recursiveDirectoryCopy()](DrupalWebTestCase/recursiveDirectoryCopy.md) — Recursively copy one directory to another.
- [setUp()](DrupalWebTestCase/setUp.md) — Sets up a Drupal site for running functional and integration tests.
- [preloadRegistry()](DrupalWebTestCase/preloadRegistry.md) — Preload the registry from the testing site.
- [resetAll()](DrupalWebTestCase/resetAll.md) — Reset all data structures after having enabled new modules.
- [refreshVariables()](DrupalWebTestCase/refreshVariables.md) — Refresh the in-memory set of variables. Useful after a page request is made that changes a variable in a different thread.
- [tearDown()](DrupalWebTestCase/tearDown.md) — Delete created files and temporary files directory, delete the tables created by setUp(), and reset the database prefix.
- [curlInitialize()](DrupalWebTestCase/curlInitialize.md) — Initializes the cURL connection.
- [curlExec()](DrupalWebTestCase/curlExec.md) — Initializes and executes a cURL request.
- [curlHeaderCallback()](DrupalWebTestCase/curlHeaderCallback.md) — Reads headers and registers errors received from the tested site.
- [curlClose()](DrupalWebTestCase/curlClose.md) — Close the cURL handler and unset the handler.
- [parse()](DrupalWebTestCase/parse.md) — Parse content returned from curlExec using DOM and SimpleXML.
- [drupalGet()](DrupalWebTestCase/drupalGet.md) — Retrieves a Drupal path or an absolute path.
- [drupalGetAJAX()](DrupalWebTestCase/drupalGetAJAX.md) — Retrieve a Drupal path or an absolute path and JSON decode the result.
- [drupalPost()](DrupalWebTestCase/drupalPost.md) — Execute a POST request on a Drupal page. It will be done as usual POST request with SimpleBrowser.
- [drupalPostAJAX()](DrupalWebTestCase/drupalPostAJAX.md) — Execute an Ajax submission.
- [cronRun()](DrupalWebTestCase/cronRun.md) — Runs cron in the Drupal installed by Simpletest.
- [checkForMetaRefresh()](DrupalWebTestCase/checkForMetaRefresh.md) — Check for meta refresh tag and if found call drupalGet() recursively. This function looks for the http-equiv attribute to be set to "Refresh" and is case-sensitive.
- [drupalHead()](DrupalWebTestCase/drupalHead.md) — Retrieves only the headers for a Drupal path or an absolute path.
- [handleForm()](DrupalWebTestCase/handleForm.md) — Handle form input related to drupalPost(). Ensure that the specified fields exist and attempt to create POST data in the correct manner for the particular field type.
- [buildXPathQuery()](DrupalWebTestCase/buildXPathQuery.md) — Builds an XPath query.
- [xpath()](DrupalWebTestCase/xpath.md) — Perform an xpath search on the contents of the internal browser. The search is relative to the root element (HTML tag normally) of the page.
- [getAllOptions()](DrupalWebTestCase/getAllOptions.md) — Get all option elements, including nested options, in a select.
- [assertLink()](DrupalWebTestCase/assertLink.md) — Pass if a link with the specified label is found, and optional with the specified index.
- [assertNoLink()](DrupalWebTestCase/assertNoLink.md) — Pass if a link with the specified label is not found.
- [assertLinkByHref()](DrupalWebTestCase/assertLinkByHref.md) — Pass if a link containing a given href (part) is found.
- [assertNoLinkByHref()](DrupalWebTestCase/assertNoLinkByHref.md) — Pass if a link containing a given href (part) is not found.
- [clickLink()](DrupalWebTestCase/clickLink.md) — Follows a link by name.
- [getAbsoluteUrl()](DrupalWebTestCase/getAbsoluteUrl.md) — Takes a path and returns an absolute path.
- [getUrl()](DrupalWebTestCase/getUrl.md) — Get the current URL from the cURL handler.
- [drupalGetHeaders()](DrupalWebTestCase/drupalGetHeaders.md) — Gets the HTTP response headers of the requested page. Normally we are only interested in the headers returned by the last request. However, if a page is redirected or HTTP authentication is in use, multiple requests will be required to retrieve the page. Headers from all requests may be requested by passing TRUE to this function.
- [drupalGetHeader()](DrupalWebTestCase/drupalGetHeader.md) — Gets the value of an HTTP response header. If multiple requests were required to retrieve the page, only the headers from the last request will be checked by default. However, if TRUE is passed as the second argument, all requests will be processed from last to first until the header is found.
- [drupalGetContent()](DrupalWebTestCase/drupalGetContent.md) — Gets the current raw HTML of requested page.
- [drupalGetSettings()](DrupalWebTestCase/drupalGetSettings.md) — Gets the value of the Drupal.settings JavaScript variable for the currently loaded page.
- [drupalGetMails()](DrupalWebTestCase/drupalGetMails.md) — Gets an array containing all e-mails sent during this test case.
- [drupalSetContent()](DrupalWebTestCase/drupalSetContent.md) — Sets the raw HTML content. This can be useful when a page has been fetched outside of the internal browser and assertions need to be made on the returned page.
- [drupalSetSettings()](DrupalWebTestCase/drupalSetSettings.md) — Sets the value of the Drupal.settings JavaScript variable for the currently loaded page.
- [assertUrl()](DrupalWebTestCase/assertUrl.md) — Pass if the internal browser's URL matches the given path.
- [assertRaw()](DrupalWebTestCase/assertRaw.md) — Pass if the raw text IS found on the loaded page, fail otherwise. Raw text refers to the raw HTML that the page generated.
- [assertNoRaw()](DrupalWebTestCase/assertNoRaw.md) — Pass if the raw text is NOT found on the loaded page, fail otherwise. Raw text refers to the raw HTML that the page generated.
- [assertText()](DrupalWebTestCase/assertText.md) — Pass if the text IS found on the text version of the page. The text version is the equivalent of what a user would see when viewing through a web browser. In other words the HTML has been filtered out of the contents.
- [assertNoText()](DrupalWebTestCase/assertNoText.md) — Pass if the text is NOT found on the text version of the page. The text version is the equivalent of what a user would see when viewing through a web browser. In other words the HTML has been filtered out of the contents.
- [assertTextHelper()](DrupalWebTestCase/assertTextHelper.md) — Helper for assertText and assertNoText.
- [assertUniqueText()](DrupalWebTestCase/assertUniqueText.md) — Pass if the text is found ONLY ONCE on the text version of the page.
- [assertNoUniqueText()](DrupalWebTestCase/assertNoUniqueText.md) — Pass if the text is found MORE THAN ONCE on the text version of the page.
- [assertUniqueTextHelper()](DrupalWebTestCase/assertUniqueTextHelper.md) — Helper for assertUniqueText and assertNoUniqueText.
- [assertPattern()](DrupalWebTestCase/assertPattern.md) — Will trigger a pass if the Perl regex pattern is found in the raw content.
- [assertNoPattern()](DrupalWebTestCase/assertNoPattern.md) — Will trigger a pass if the perl regex pattern is not present in raw content.
- [assertTitle()](DrupalWebTestCase/assertTitle.md) — Pass if the page title is the given string.
- [assertNoTitle()](DrupalWebTestCase/assertNoTitle.md) — Pass if the page title is not the given string.
- [assertThemeOutput()](DrupalWebTestCase/assertThemeOutput.md) — Asserts themed output.
- [assertFieldByXPath()](DrupalWebTestCase/assertFieldByXPath.md) — Asserts that a field exists in the current page by the given XPath.
- [getSelectedItem()](DrupalWebTestCase/getSelectedItem.md) — Get the selected value from a select field.
- [assertNoFieldByXPath()](DrupalWebTestCase/assertNoFieldByXPath.md) — Asserts that a field doesn't exist or its value doesn't match, by XPath.
- [assertFieldByName()](DrupalWebTestCase/assertFieldByName.md) — Asserts that a field exists in the current page with the given name and value.
- [assertNoFieldByName()](DrupalWebTestCase/assertNoFieldByName.md) — Asserts that a field does not exist with the given name and value.
- [assertFieldById()](DrupalWebTestCase/assertFieldById.md) — Asserts that a field exists in the current page with the given ID and value.
- [assertNoFieldById()](DrupalWebTestCase/assertNoFieldById.md) — Asserts that a field does not exist with the given ID and value.
- [assertFieldChecked()](DrupalWebTestCase/assertFieldChecked.md) — Asserts that a checkbox field in the current page is checked.
- [assertNoFieldChecked()](DrupalWebTestCase/assertNoFieldChecked.md) — Asserts that a checkbox field in the current page is not checked.
- [assertOptionSelected()](DrupalWebTestCase/assertOptionSelected.md) — Asserts that a select option in the current page is checked.
- [assertNoOptionSelected()](DrupalWebTestCase/assertNoOptionSelected.md) — Asserts that a select option in the current page is not checked.
- [assertField()](DrupalWebTestCase/assertField.md) — Asserts that a field exists with the given name or ID.
- [assertNoField()](DrupalWebTestCase/assertNoField.md) — Asserts that a field does not exist with the given name or ID.
- [assertNoDuplicateIds()](DrupalWebTestCase/assertNoDuplicateIds.md) — Asserts that each HTML ID is used for just a single element.
- [constructFieldXpath()](DrupalWebTestCase/constructFieldXpath.md) — Helper function: construct an XPath for the given set of attributes and value.
- [assertResponse()](DrupalWebTestCase/assertResponse.md) — Asserts the page responds with the specified response code.
- [assertNoResponse()](DrupalWebTestCase/assertNoResponse.md) — Asserts the page did not return the specified response code.
- [assertMail()](DrupalWebTestCase/assertMail.md) — Asserts that the most recently sent e-mail message has the given value.
- [assertMailString()](DrupalWebTestCase/assertMailString.md) — Asserts that the most recently sent e-mail message has the string in it.
- [assertMailPattern()](DrupalWebTestCase/assertMailPattern.md) — Asserts that the most recently sent e-mail message has the pattern in it.
- [verboseEmail()](DrupalWebTestCase/verboseEmail.md) — Outputs to verbose the most recent $count emails sent.

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
