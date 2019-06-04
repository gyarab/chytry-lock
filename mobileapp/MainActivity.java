package com.example.smartlock10;

import android.annotation.SuppressLint;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Html;
import android.view.KeyEvent;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.inputmethod.EditorInfo;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.example.programmingknowledge.easyonlineconverter.R;

import org.w3c.dom.Text;


public class MainActivity extends AppCompatActivity {
    private WebView myWebView;
    private Button btn;
    private EditText editText;
    private String s = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        editText =  findViewById(R.id.edittext);
        btn = findViewById(R.id.button5);
        btn.setText(Html.fromHtml("&#x1F50D"));
        myWebView = (WebView) findViewById(R.id.webView);
        WebSettings webSettings = myWebView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        btn.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                s = editText.getText().toString();
                myWebView.loadUrl("http://"+s+"/");

            }
        });
        myWebView.setWebViewClient(new WebViewClient());

    }

    @Override
    public void onBackPressed() {
        if (myWebView.canGoBack()) {
            myWebView.goBack();
        } else {
            super.onBackPressed();
        }
    }
}
