import { createRoot } from "react-dom/client";
import React from "react";
import { rootStore, RootStoreProvider } from "./store";
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { ConfigProvider } from "antd";
import "./index.css";
import ru_RU from 'antd/locale/ru_RU';
import 'dayjs/locale/ru';
import dayjs from 'dayjs'

import { App } from "./layouts/App"




dayjs.locale('ru')
const root = createRoot(document.getElementById("root"));

root.render(

    <RootStoreProvider store={rootStore}>
      <BrowserRouter>
        <ConfigProvider locale={ru_RU}>
          <App />
        </ConfigProvider>
      </BrowserRouter>
    </RootStoreProvider>

);
